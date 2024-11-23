import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from mlxtend.frequent_patterns import apriori, association_rules


if __name__ == "__main__":
    # Step 1: Create dummy data (20 rows)
    np.random.seed(42)
    customer_ids = [f'customer_{i}' for i in range(1, 21)]
    product_types = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    purchase_dates = pd.date_range('2023-01-01', periods=20, freq='D').tolist()
    age = np.random.randint(18, 65, size=20)
    gender = np.random.choice(['Male', 'Female'], size=20)

    # Random purchases for each customer
    data = []
    for customer_id in customer_ids:
        num_purchases = np.random.randint(1, 4)  # Each customer will make 1 to 3 purchases
        purchases = np.random.choice(product_types, num_purchases, replace=True)
        purchase_dates_for_customer = np.random.choice(purchase_dates, num_purchases, replace=False)
        for i in range(num_purchases):
            data.append(
                [customer_id, purchases[i], purchase_dates_for_customer[i], age[customer_ids.index(customer_id)],
                 gender[customer_ids.index(customer_id)]])

    df = pd.DataFrame(data, columns=['customer_id', 'product_type', 'purchase_date', 'age', 'gender'])
    df['purchase_date'] = pd.to_datetime(df['purchase_date'])

    # Step 2: Clustering customers based on age and gender
    df_cluster = df[['age', 'gender']].copy()
    df_cluster['gender'] = df_cluster['gender'].map({'Male': 0, 'Female': 1})  # Encoding gender

    kmeans = KMeans(n_clusters=3, random_state=42)
    df_cluster['cluster_id'] = kmeans.fit_predict(df_cluster[['age', 'gender']])

    # Adding cluster_id to the main dataframe
    df['cluster_id'] = df_cluster['cluster_id']

    # Step 3: Sort by customer_id and purchase_date to determine transaction sequence
    df_sorted = df.sort_values(by=['customer_id', 'purchase_date'])

    # Function to get sequential transactions, considering same-day purchases as part of the same transaction
    def get_sequential_transactions(df_sorted):
        sequential_data = []
        # Iterate over each customer
        for customer_id, group in df_sorted.groupby('customer_id'):
            # Group products by purchase date for this customer
            date_grouped = group.groupby('purchase_date')['product_type'].apply(list).reset_index()
            # For each date, consider it as a separate transaction
            for i, row in date_grouped.iterrows():
                sequential_data.append({'customer_id': customer_id, 'sequence': i + 1, 'products': row['product_type'],
                                        'purchase_date': row['purchase_date']})
        return pd.DataFrame(sequential_data)

    # Getting the sequential transactions considering same-day purchases
    sequential_transactions = get_sequential_transactions(df_sorted)


    # Step 4: Apply Apriori to recommend products for each sequence
    def apply_apriori(sequential_transactions, sequence_number):
        # Filter the data for the given sequence (1st, 2nd, or 3rd)
        seq_data = sequential_transactions[sequential_transactions['sequence'] == sequence_number]

        # One-hot encoding of the products for the Apriori algorithm
        oht_data = pd.get_dummies(pd.DataFrame(seq_data['products'].tolist(), dtype=object), dtype=bool)

        # Apply Apriori algorithm to find frequent itemsets
        frequent_itemsets = apriori(oht_data, min_support=0.01, use_colnames=True)

        # Generate association rules from frequent itemsets
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.0000001)

        return rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]


    def recommend_products_by_sequence(sequential_transactions, sequence_number):
        # Step 1: Filter the data for the given sequence (1st, 2nd, or 3rd transaction)
        seq_data = sequential_transactions[sequential_transactions['sequence'] == sequence_number]

        # Step 2: One-hot encode the product data for Apriori
        oht_data = pd.get_dummies(pd.DataFrame(seq_data['products'].tolist(), dtype=object), dtype=bool)

        # Step 3: Apply Apriori to find frequent itemsets
        frequent_itemsets = apriori(oht_data, min_support=0.1, use_colnames=True)

        # Step 4: Sort by support to get the most frequent itemsets
        sorted_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)

        return sorted_itemsets[['itemsets', 'support']]

    # Step 5: Generate product recommendations for each sequence
    # Recommend for first purchases
    first_purchase_rules = recommend_products_by_sequence(sequential_transactions, 1)
    print("First Purchase Recommendations:")
    print(first_purchase_rules)

    # Recommend for second purchases
    second_purchase_rules = recommend_products_by_sequence(sequential_transactions, 2)
    print("\nSecond Purchase Recommendations:")
    print(second_purchase_rules)

    # Recommend for third purchases
    third_purchase_rules = recommend_products_by_sequence(sequential_transactions, 3)
    print("\nThird Purchase Recommendations:")
    print(third_purchase_rules)





