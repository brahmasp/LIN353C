# Homework 7
# Name: Brahma S. Pavse
# UT EID: bsp686


# Problem 1
'''

1.NASA puts the Earth up for adoption

Reading 1: Makes it seem like the NASA is a parent that is putting the earth up for adoption

Reading 2: In reality its just a way for supporters to get scientific information about the some specific place on earth

Tagging: NASA/NNP puts/V the/DT Earth/NNP up/P for/P adoption/NN

In this case the POS tagging does not help in distinguishing between someone actually
owning the land (or part) of the earth from just receiving personal scientific information
about it.

2. Look up! Do not miss this week's 'Pink Moon'

Reading 1: Makes it seem like there exists a pink moon

Reading 2: In reality it is just an April full moon

Tagging: Look/V up/P Do/V not/RB miss/V this/DT week's/NN Pink Moon/NNP

Yes the POS taggings help. With the tagging, we know that Pink Moon is
proper noun, instead of labelling the color of the moon as pink.


3. Delta meltdown

Reading 1: Delta airline failure

Reading 2: Delta company melted down

Tagging: Delta/NNP meltdown/NN

No the POS does not necessarily clear it up. We stll do not know if Delta 
literally melted down or if they suffered a catastrophic situation (well it is
but catastrophic situation could mean financially as well).

'''


# Problem 2


'''

(a)

v0(START) = 1

1.

Sequence DT and corresponding word "the"

v1(DT) = P(START) * P(DT|START) * P(the|DT) = 1 * 0.14 * 0.63
		= 0.0882


2.

Sequence DT JJ and corresponding word "the complex"

v2(JJ) = v(DT) * P(JJ|DT) * P(complex|JJ)
	= 0.0882 * 0.23 * 0.0008
	= 1.622883e-05

Sequence DT NN and corresponding word "the complex"

v2(NN) = v(DT) * P(NN|DT) * P(complex|NN)
	= 0.0882 * 0.61 * 0.0001
	= 0.00000538

3.

Sequence DT JJ NN and corresponding word "the complex houses"

v3(NN) = v(JJ) * P(NN|JJ) * P(houses|NN)
	= 1.622883e-05 * 0.64 * 0.0003
	= 3.11593536e-09 (max)

Sequence DT NN NN and corresponding word "the complex houses"

v3(NN) = v(NN) * P(NN|NN) * P(houses|NN)
	= 0.00000538 * 0.1 * 0.0003
	= 1.614e-10 (min)

Sequence DT JJ VB corresponding word "the complex houses"

v3(VB) = v(JJ) * P(VB|JJ) * P(houses|VB)
	= 0.000016229 * 0.01 * 0.00003
	= 4.8687e-12 (min)

Sequence DT NN VB and corresponding word "the complex houses"

v3(VB) = v(NN) * P(VB|NN) * P(houses|VB)
	= 0.00000538 * 0.06 * 0.00003
	= 9.68401e-12 (max)

4. 

Sequence DT JJ NN NN and "the complex houses students"

v4(NN) = v(NN) * P(NN|NN) * P(students|NN)
	= 3.11593536e-09 * 0.1 * 0.0009
	= 2.7E-13


Sequence DT NN VB NN and "the complex houses sutdents"

v4(NN) = v(VB) * P(NN|VB) * P(students|NN)
	= 9.684000000000001e-12  * 0.11 * 0.0009
	= 9.58716E-16


(b)

The most likely is the mapping
START -> DT -> JJ -> NN -> NN

After setting up the terrilis, the max verterbi number v4(NN)
is based on v3(NN), which is based on v2(JJ) which is based on
v1(DT).

'''


