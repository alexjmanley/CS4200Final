import kagglehub

path = kagglehub.dataset_download(
        "alitaqishah/iran-war-oil-shock-2026-brent-and-gas-tracker",
        output_dir="./data")

print("Path to dataset files:", path)
