import matplotlib.pyplot as plt
import adjustText as aT

print("Plotting in progress..... Two maps will be created shortly, one for the\n"
      "sellers and one for the buyers. Thank you for your patience")

#PLOTS MAP OF SELLERS

ax = state_sellers.plot(column='n_arms', zorder=2, figsize=(32, 16), linewidth=0.1, edgecolor='white', cmap='RdBu', legend=True)
az = borders_world.plot(ax=ax, color="grey", edgecolor='white', linewidth=0.1, zorder=1)
agg_year_conflicts.plot(ax=ax, c = "green", markersize= 'years_in_conflict', alpha=0.7, categorical=False, legend=False,
                        zorder=3)

texts = []

for x, y, label in zip(centroids_states.geometry.x, centroids_states.geometry.y, centroids_states.NAME_ENGL):
    texts.append(plt.text(x, y, label, fontsize=4))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), textcoords="offset points")

plt.savefig('map_export.pdf', dpi=400)
plt.show()

#PLOTS MAP OF BUYERS

ax = state_buyers.plot(column='n_arms', zorder=2, figsize=(32, 16), linewidth=0.1, edgecolor='white', cmap='RdBu', legend=True)
az = borders_world.plot(ax=ax, color="grey", edgecolor='white', linewidth=0.1, zorder=1)
agg_year_conflicts.plot(ax=ax, c = "green", markersize= 'years_in_conflict', alpha=0.7, categorical=False, legend=False,
                        zorder=3)

texts = []

for x, y, label in zip(centroids_states.geometry.x, centroids_states.geometry.y, centroids_states.NAME_ENGL):
    texts.append(plt.text(x, y, label, fontsize=4))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(1,1), expand_text=(1,1), textcoords="offset points")

plt.savefig('map_import.pdf', dpi=400)
plt.show()

engine.dispose()

