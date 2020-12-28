import json
import numpy as np


with open('input.json', 'r') as f:
    inputs = json.load(f)

allocs = []
errors = []

for p in range(101):
    p /= 100
    ps = dict(stock=p, bonds=round(1-p, 2))

    new_val_stock = inputs['current_values']['stock'] + ps['stock']*inputs['new_investment']
    new_val_bonds = inputs['current_values']['bonds'] + ps['bonds']*inputs['new_investment']

    new_alloc_stock = new_val_stock / (new_val_stock + new_val_bonds)
    error = abs(inputs['target_allocation']['stock'] - new_alloc_stock)

    allocs.append(ps)
    errors.append(error)

best_alloc_idx = np.argmin(errors)
best_alloc = allocs[best_alloc_idx]

print()
print('Current allocation:')
curr_val_stock = inputs['current_values']['stock']
curr_val_bonds = inputs['current_values']['bonds']
curr_val = curr_val_stock + curr_val_bonds
curr_alloc_stock = curr_val_stock / curr_val * 100
print(f'  - Stock: {curr_val_stock} ({curr_alloc_stock:.1f})')
print(f'  - Bonds: {curr_val_bonds} ({100-curr_alloc_stock:.1f})')
print()
print(f'Incoming money: {inputs["new_investment"]:.0f}')
print()
print('Need to buy:')
print(f'  - Stock: {best_alloc["stock"]*100:.0f}%')
print(f'  - Bonds: {best_alloc["bonds"]*100:.0f}%')
print()
print('After buying, you will have:')
new_val_stock = inputs['current_values']['stock'] + best_alloc['stock']*inputs['new_investment']
new_val_bonds = inputs['current_values']['bonds'] + best_alloc['bonds']*inputs['new_investment']
new_val = new_val_stock + new_val_bonds
new_alloc_stock = new_val_stock / new_val * 100
print(f'  - Stock: {new_val_stock} ({new_alloc_stock:.1f}%)')
print(f'  - Bonds: {new_val_bonds} ({100-new_alloc_stock:.1f}%)')
