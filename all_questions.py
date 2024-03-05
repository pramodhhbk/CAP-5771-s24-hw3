# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "While k-means assigns points to centroids, making it sensitive to outliers' influence on centroid positions, agglomerative hierarchical clustering merges clusters based on proximity. This gradual merging creates a hierarchical structure and effectively mitigates the influence of outliers by grouping them with nearby points."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "In k-means, the initial placement of centroids is random, leading to diverse clusterings across different runs. Conversely, agglomerative hierarchical clustering consistently generates the same clustering as it follows a deterministic approach of merging clusters based on proximity."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While k-means is typically more computationally efficient and memory-friendly than agglomerative hierarchical clustering for large datasets, it's inaccurate to assert it as the most efficient clustering algorithm overall. Other algorithms may outperform k-means under specific conditions or offer advantages in particular scenarios."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "The sum of squared errors (SSE) in clustering usually decreases as clusters split, allowing centroids to better represent data points within smaller clusters, thereby reducing distances between data points and their respective centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "A decline in the Sum of Squared Errors (SSE) during k-means clustering signifies data points within each cluster moving closer to their respective centroids, indicating enhanced cohesion within clusters."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "An upsurge in the Sum of Squared Between (SSB) suggests centroids moving farther apart from each other, indicating greater separation between clusters."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Enhancing cohesion in k-means clustering typically results in increased separation, as tightly clustered data points within clusters make centroids more distinct from each other."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "When clustering data with k-means, the sum of within-cluster sum of squares (SSE) and between-cluster sum of squares (BSS) remains constant, equaling the total sum of squares (TSS)."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Improving cohesion in k-means clustering typically leads to increased separation, as tightly clustered data points within clusters make centroids more distinct from each other"

    return answers






# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4 * (R**2)"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4 * (a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10 * (R**2)"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The centroids in Circle B will move towards the centroids of Circle A and Circle C because the points are evenly spread within each circle. As a result, after convergence, each circle will have one centroid as they adjust to balance the points in each circle."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Circle A will keep its centroid because of its evenly distributed points. Circle B, starting with two centroids, may shift one towards Circle C for balance. Circle C, starting with none, will gain one from Circle B. So, after convergence, each circle will have one centroid."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "As Circles A and B are close, the centroid from Circle A might move towards the midpoint between A and B in k-means. Circle C, farther from B, may not affect centroid redistribution much and keeps its two centroids."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A','Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B will merge because the distance from the farthest right point in A to the furthest left point in B is shorter than the distances between A and C, as well as between B and C"

    # type: set
    answers["(b)"] = {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Due to their shortest complete link distance, measured from a boundary point of A to the farthest point in C, groups A and C combine. This distance is shorter than the complete link distances between A and B (from A's left-most to B's right-most point) and between B and C (from B's right-most to C's farthest point)."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E', 'B', 'F', 'J', 'C', 'L', 'M', 'I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M' }

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 exhibits the highest clustering entropy due to its more evenly distributed objects across various classes compared to the other clusters."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "With one class significantly outnumbering others, the cluster exhibits dominance, resulting in lower entropy."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Each diagonal entry displays a clear and predominant blue color, suggesting a high level of cohesion within clusters. This indicates that points within the same cluster are tightly clustered together, ensuring consistent coherence within each cluster."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Rows 1 and 3 correspond to clusters A and C, respectively, distinguished by the varying colors in the off-diagonal entries. Similarly, rows 2 and 4 are associated with clusters B and D, respectively, presenting analogous observations."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The clear and predominantly blue characteristics of diagonal entries stand out, distinguishing themselves from others. This indicates a high level of cohesion within clusters B and C."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows 1 and 4 show varied colors, suggesting different distances from other clusters, with less defined diagonal entries. Rows 2 and 3 display two identical colors, indicating equidistant relationships with two clusters and a greater distance from one cluster."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Two diagonal entries, notably clear and intense in blue color, indicate strong cohesion within clusters B and C. This uniformity implies stronger intra-cluster relationships within these clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Each row features two off-diagonal entries with matching colors, while one entry differs in color, indicating that each cluster is relatively closer to two other clusters compared to the third."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "All off-diagonal entries display different colors, signifying diverse distances from other clusters. Cluster A, with a less defined diagonal entry, indicates weaker cohesion within."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Row 2 is Cluster B, as two out of three off-diagonal entries have matching colors, indicating equidistant relationships, notably between B and A, and B and C. The clearer diagonal entry suggests robust cohesion within this cluster, contrasting with B's distance from D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Row 3 represents Cluster C, as indicated by the clearer diagonal entry, suggesting robust cohesion within this cluster. Two out of three off-diagonal entries exhibit matching colors, highlighting equidistant relationships, particularly between C and B, and C and D. Notably, C is farther from A in comparison."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Cluster D is discernible due to its off-diagonal entries displaying different colors, denoting varying distances from other clusters. Notably, D exhibits varying distances from other clusters, being closest to C, then B, and farthest from A. The less defined diagonal entry implies weaker cohesion within this cluster, confirming its classification as Cluster D"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical','overlapping','partial']

    # type: list
    answers["(b)"] = ['partitional','exclusive','complete']

    # type: list
    answers["(c)"] = ['partitional','fuzzy','complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping','partial']

    # type: list
    answers["(e)"] = ['partitional','exclusive','partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Students with similar scores and mark levels can also be grouped together in a hierarchical structure."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Points within the nose, eyes, and mouth regions are much closer to each other compared to points between these areas."

    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means would identify the nose, eyes, and mouth regions, but it would also encompass the lower density points."

    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
