import pandas as pd


def calculate_group_metrics(df, group_col):
    """
    Calculates key marketing metrics by group.

    Parameters:
        df: pandas DataFrame
        group_col: column used to group the data, such as image_type

    Returns:
        pandas DataFrame with summary metrics.
    """

    summary = df.groupby(group_col).agg(
        users=("user_id", "count"),
        clicks=("clicks", "sum"),
        ctr=("clicks", "mean"),
        conversions=("converted", "sum"),
        conversion_rate=("converted", "mean"),
        avg_time_on_page=("time_on_page", "mean"),
        revenue=("purchase_value", "sum"),
        revenue_per_user=("purchase_value", "mean")
    )

    return summary

def calculate_lift(summary_df, treatment_group, control_group):
    """
    Calculates relative lift between treatment and control groups.

    Parameters:
        summary_df: DataFrame returned by calculate_group_metrics
        treatment_group: group expected to perform better
        control_group: baseline group

    Returns:
        Dictionary with lift values.
    """

    treatment = summary_df.loc[treatment_group]
    control = summary_df.loc[control_group]

    return {
        "ctr_lift": float((treatment["ctr"] - control["ctr"]) / control["ctr"]),
        "conversion_lift": float((treatment["conversion_rate"] - control["conversion_rate"]) / control["conversion_rate"]),
        "revenue_per_user_lift": float((treatment["revenue_per_user"] - control["revenue_per_user"]) / control["revenue_per_user"])
    }

if __name__ == "__main__":
    df = pd.read_csv("data/raw/ab_visual_assets.csv")

    summary = calculate_group_metrics(
        df=df,
        group_col="image_type"
    )

    print(summary)

    lift = calculate_lift(
        summary_df=summary,
        treatment_group="lifestyle",
        control_group="studio"
    )

    print("\nLift:")
    print(lift)