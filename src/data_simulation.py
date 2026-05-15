import pandas as pd
import numpy as np

def generate_ab_test_data(n_users=10000, random_state=42):
    np.random.seed(random_state)
    user_ids = np.arange(1, n_users + 1)

    image_types = np.random.choice(["studio", "lifestyle"],size=n_users,p=[0.5, 0.5])

    genders = np.random.choice(["male","female"],size=n_users,p=[0.48, 0.52])

    age_groups = np.random.choice(["young","adult","senior"],size=n_users,p=[0.35,0.50,0.15])

    customer_types = np.random.choice(
        ["new", "returning"],
        size=n_users,
        p=[0.65, 0.35]
    )

    #Clicks
    
    click_probabilities = np.where(
        image_types == "lifestyle",
        0.10,
        0.08
    )

    click_probabilities += np.where(
        customer_types == "returning",
        0.02,
        0.00
    )

    click_probabilities += np.where(
        (age_groups == "young") & (image_types == "lifestyle"),
        0.015,
        0.00
    )

    click_probabilities += np.where(
        age_groups == "senior",
        -0.01,
        0.00
    )

    click_probabilities = np.clip(click_probabilities, 0, 1)

    clicks = np.random.binomial(
        n=1,
        p=click_probabilities,
        size=n_users
    )

    #Conversion

    conversion_probabilities = np.where(
        image_types == "lifestyle",
        0.04,
        0.03
    )

    conversion_probabilities += np.where(
        customer_types == "returning",
        0.015,
        0.00
    )

    conversion_probabilities += np.where(
        clicks == 1,
        0.05,
        0.00
    )

    conversion_probabilities += np.where(
        age_groups == "senior",
        -0.005,
        0.00
    )

    conversion_probabilities = np.clip(conversion_probabilities, 0, 1)

    converted = np.random.binomial(
        n=1,
        p=conversion_probabilities,
        size=n_users
    )

    #Time on Page

    base_time_on_page = np.where(
        image_types == "lifestyle",
        42,
        35
    )

    base_time_on_page += np.where(
        clicks == 1,
        15,
        0
    )

    base_time_on_page += np.where(
        converted == 1,
        20,
        0
    )

    base_time_on_page += np.where(
        age_groups == "senior",
        5,
        0
    )

    time_on_page = np.random.normal(
        loc=base_time_on_page,
        scale=10,
        size=n_users
    )

    time_on_page = np.clip(time_on_page, 1, None)
    time_on_page = np.round(time_on_page, 2)

    #Purchase value

    base_purchase_value = np.where(
        converted == 1,
        120,
        0
    )

    base_purchase_value += np.where(
        (converted == 1) & (customer_types == "returning"),
        20,
        0
    )

    base_purchase_value += np.where(
        (converted == 1) & (image_types == "lifestyle"),
        10,
        0
    )

    purchase_value = np.where(
        converted == 1,
        np.random.normal(
            loc=base_purchase_value,
            scale=30,
            size=n_users
        ),
        0
    )

    purchase_value = np.clip(purchase_value, 0, None)
    purchase_value = np.round(purchase_value, 2)



    df = pd.DataFrame({
        "user_id": user_ids,
        "image_type": image_types,
        "gender": genders,
        "age_group": age_groups,
        "customer_type": customer_types,
        "clicks": clicks,
        "converted": converted,
        "time_on_page": time_on_page,
        "purchase_value": purchase_value
    })

    return df

if __name__ == "__main__":
    df = generate_ab_test_data()
    print(df.head())
    print(df["image_type"].value_counts())

    print("\nCTR by image type:")
    ctr_by_image = df.groupby("image_type")["clicks"].mean()
    print(ctr_by_image)

    print("\nCTR by image type and age group:")
    ctr_by_segment = df.groupby(["image_type", "age_group"])["clicks"].mean()
    print(ctr_by_segment)

    print("\nCTR by image type and customer type:")
    ctr_by_customer_type = df.groupby(["image_type", "customer_type"])["clicks"].mean()
    print(ctr_by_customer_type)

    print("\nConversion rate by image type:")
    conversion_by_image = df.groupby("image_type")["converted"].mean()
    print(conversion_by_image)

    print("\nConversion rate by image type and age group:")
    conversion_by_segment = df.groupby(["image_type", "age_group"])["converted"].mean()
    print(conversion_by_segment)

    print("\nConversion rate by image type and customer type:")
    conversion_by_customer_type = df.groupby(["image_type", "customer_type"])["converted"].mean()
    print(conversion_by_customer_type)

    print("\nAverage time on page by image type:")
    time_by_image = df.groupby("image_type")["time_on_page"].mean()
    print(time_by_image)

    print("\nAverage time on page by image type and customer type:")
    time_by_customer_type = df.groupby(["image_type", "customer_type"])["time_on_page"].mean()
    print(time_by_customer_type)

    print("\nAverage purchase value by image type:")
    avg_purchase_by_image = df.groupby("image_type")["purchase_value"].mean()
    print(avg_purchase_by_image)

    print("\nAverage purchase value among converted users by image type:")
    avg_purchase_converted = df[df["converted"] == 1].groupby("image_type")["purchase_value"].mean()
    print(avg_purchase_converted)

    print("\nTotal revenue by image type:")
    revenue_by_image = df.groupby("image_type")["purchase_value"].sum()
    print(revenue_by_image)

    df.to_csv("data/raw/ab_visual_assets.csv", index=False)
    print("\nDataset saved at: data/raw/ab_visual_assets.csv")