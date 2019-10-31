from matplotlib_venn import venn2
from matplotlib import pyplot

# venn = venn2(subsets=(53, 20, 46), alpha=0.9, set_colors=('royalblue', 'tomato'))
# for text in venn.set_labels:
#     text.set_fontsize(25)
# for text in venn.subset_labels:
#     text.set_fontsize(25)

# set11 = venn.get_patch_by_id('11')
# set01 = venn.get_patch_by_id('01')
# set10 = venn.get_patch_by_id('10')

# set01.set_edgecolor("black")
# set11.set_edgecolor("black")
# set10.set_edgecolor("black")

# pyplot.show()


# venn = venn2(subsets=(1, 1, 1), alpha=1, set_colors=('royalblue', 'tomato'))

# for text in venn.set_labels:
#     text.set_fontsize(25)

# label10 = venn.get_label_by_id('10')
# label01 = venn.get_label_by_id('01')
# label11 = venn.get_label_by_id('11')
# label01.set_text('')
# label10.set_text('')
# label11.set_text('')

# set11 = venn.get_patch_by_id('11')
# set01 = venn.get_patch_by_id('01')
# set10 = venn.get_patch_by_id('10')
# set01.set_edgecolor("black")
# set11.set_edgecolor("black")
# set10.set_edgecolor("black")

# pyplot.show()

venn = venn2(subsets=(53, 20, 46), set_colors=('g', 'r'))
for text in venn.set_labels:
    text.set_fontsize(25)
for text in venn.subset_labels:
    text.set_fontsize(25)

set11 = venn.get_patch_by_id('11')
set01 = venn.get_patch_by_id('01')
set10 = venn.get_patch_by_id('10')

set01.set_edgecolor("black")
set11.set_edgecolor("black")
set10.set_edgecolor("black")

# pyplot.show()
pyplot.savefig("venn.png", transparent=True)


venn = venn2(subsets=(1, 1, 1), set_colors=('g', 'r'))

for text in venn.set_labels:
    text.set_fontsize(25)

label10 = venn.get_label_by_id('10')
label01 = venn.get_label_by_id('01')
label11 = venn.get_label_by_id('11')
label01.set_text('')
label10.set_text('')
label11.set_text('')

set11 = venn.get_patch_by_id('11')
set01 = venn.get_patch_by_id('01')
set10 = venn.get_patch_by_id('10')
set01.set_edgecolor("black")
set11.set_edgecolor("black")
set10.set_edgecolor("black")

# pyplot.show()
