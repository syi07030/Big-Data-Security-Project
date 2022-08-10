with open('/*fileIn path*/', 'r') as f:
    data = f.read().split()

max_cols = 2586

for id, row in enumerate(data):
    if cols[id] < max_cols:
        data[id] += (max_cols - cols[id]) * ','

with open('/*fileOut path*/', 'w') as f:
    f.write('\n'.join(data))