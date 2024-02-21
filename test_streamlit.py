import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Main Streamlit app code
def main():
    st.title('Scatter Chart Analysis')
    plt.rcParams['interactive'] = True

    # Upload CSV file
    csv_file = st.file_uploader('Upload CSV File', type=['csv'])
    if csv_file is not None:
        try:
            # Read DataFrame from CSV file
            df = pd.read_csv(csv_file)

            # Remove null values
            df.dropna(inplace=True)

            # Check if 'type' column has 10 distinct values
            st.write('### Scatter Plot')
            fig, ax = plt.subplots(figsize=(10, 6))
            for t in df['type'].unique():
                subset_df = df[df['type'] == t]
                ax.scatter(subset_df['request_id'], subset_df['difference'], label=t)

            ax.scatter(df['request_id'], df['difference'], c='blue', alpha=0.5)
            ax.set_xlabel('Request ID')
            ax.set_ylabel('Difference')
            ax.set_title('Scatter Plot of Request ID vs Difference')
            st.pyplot(fig)

            # Generate shareable report
            # Generate shareable report
            st.write('### Shareable Report')
            st.write('Download the CSV file:')
            st.write(df)
            csv_download_link = f'<a href="data:text/csv;base64,{df.to_csv(index=False).encode().decode()}">Download CSV</a>'
            st.markdown(csv_download_link, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error processing CSV file: {e}")

if __name__ == '__main__':
    main()
