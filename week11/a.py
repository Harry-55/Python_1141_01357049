import pandas as pd
import numpy as np

df = pd.read_csv("aqx_p_488.csv")

while(1):
    try:
        choice = int(input("請輸入功能代碼 (1~4): "))
        if choice == 1:
            aqi_mean = df["aqi"].mean()
            aqi_max = df["aqi"].max()
            aqi_min = df["aqi"].min()
            aqi_std = df["aqi"].std()

            print(f"平均 AQI：{aqi_mean:.1f}")
            print(f"最高 AQI：{aqi_max:.1f}")
            print(f"最低 AQI：{aqi_min:.1f}")
            print(f"AQI 標準差：{aqi_std:.1f}")

        elif choice == 2:
            pm = df["pm2.5_conc"]

            pm_mean = pm.mean()
            pm_max = pm.max()
            pm_min = pm.min()
            pm_std = pm.std()
            print(f"平均 PM2.5：{pm_mean:.1f}")
            print(f"最高 PM2.5：{pm_max:.1f}")
            print(f"最低 PM2.5：{pm_min:.1f}")
            print(f"PM2.5 標準差：{pm_std:.1f}")

        elif choice == 3:
            county_aqi = df.groupby("county")["aqi"].mean().sort_values(ascending=False)

            for county, aqi in county_aqi.items():
                print(f"{county}: {aqi:.1f}")
        elif choice == 4:
            idx = df.groupby("county")["aqi"].idxmax()
            highest_rows = df.loc[idx]

            for _, row in highest_rows.iterrows():
                print(f"{row['county']} {row['sitename']} {row['aqi']:.1f} {row['datacreationdate']}")
        else:
            print("ERROR")
    except ValueError :
        print("ERROR")