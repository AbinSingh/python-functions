import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

if __name__ == "__main__":
    # Create a sample dataframe
    data = {
        "Transaction ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Items Purchased": [
            ['Milk', 'Bread'],
            ['Milk', 'Diaper', 'Beer'],
            ['Milk', 'Bread', 'Diaper'],
            ['Bread', 'Diaper', 'Eggs'],
            ['Milk', 'Eggs'],
            ['Milk', 'Bread', 'Eggs'],
            ['Bread', 'Eggs'],
            ['Diaper', 'Beer'],
            ['Milk', 'Diaper'],
            ['Milk', 'Bread', 'Diaper', 'Eggs']
        ]
    }

    df = pd.DataFrame(data)

    # Convert the transactions into a one-hot encoded dataframe
    from mlxtend.preprocessing import TransactionEncoder

    te = TransactionEncoder()
    te_data = te.fit(df['Items Purchased']).transform(df['Items Purchased'])
    df_encoded = pd.DataFrame(te_data, columns=te.columns_)

    # Apply Apriori algorithm to find frequent itemsets with minimum support of 0.3
    frequent_itemsets = apriori(df_encoded, min_support=0.3, use_colnames=True)

    # Generate association rules with minimum confidence of 0.5
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

    # Print outputs
    print("One-hot Encoded Data:")
    print(df_encoded)
    print("\nFrequent Itemsets:")
    print(frequent_itemsets)
    print("\nAssociation Rules:")
    print(rules)
