# Εργασία 1

## Θέμα 1

### Άσκηση 33, σελίδα 13

- H $\left(x_{n}\right)$ συγκλίνει στο $x \in \mathbb{R}$.
  
  
Kάθε υπακολουθία συγκλίνει στο ίδιο όριο με μια συγκλίνουσα ακολουθία. Εφaρμόζοντας το προηγούμενο θεώρημα δύο διαδοχικές φορές έχουμε ότι η υπακολουθία $\left(x_{n_{k_{l}}}\right)$ συγκλίνει στο $x \in \mathbb{R}$.
  
- Kάθε υπακολουθία $\left(x_{n_{k}}\right)$ της $\left(x_{n}\right)$ έχει μια επιπλέον υπακολουθία $\left(x_{n_{k_{l}}}\right)$ η οποία συγκλίνει στο $x \in \mathbb{R}$.


Έστω ότι η ακολουθία $\left(x_{n}\right)$  δεν συγκλίνει στο $x$. Τότε υπάρχει $\epsilon > 0$ τέτοιο ώστε για κάθε $k$ υπάρχει $n_{k}>k$ το οποίο ικανοποιεί την σχέση $\left|x_{n_{k}}-x\right| \geq \epsilon$. Αυτό γιατί αν υπήρχε $k$ το οποίο δεν είχε $n_{k}$ με την ιδιότητα της προηγούμενης πρότασης τότε απο τον ορισμό του ορίου θα έπρεπε η $\left(x_{n}\right)$ να συγκλίνει στο $x$. Άρα η υπακολουθία $\left(x_{n_{k}}\right)$ δεν έχει υπακολουθία η οποία να συγκλίνει στο $x$, το οποίο είναι άτοπο.
  
### Άσκηση 46, σελίδα 16
  
(a) Έστω $\epsilon = f(0) > 0$. Αφού $f$ συνεχής στο $x = 0$, υπάρχει $\alpha > 0$ τέτοιο ώστε για κάθε $x$ με $|x|< \alpha \iff -\alpha < x < \alpha$ έχουμε $|f(x)-f(0)|<\epsilon \implies f(x) > 0$.
  
(b) Έστω ότι υπάρχει άρρητος $x_{0}$ με $f(x_{0}) < 0$. Θεωρούμε $\epsilon = -f(x_{0}) > 0$. Αφού $f$ συνεχής στο $x_{0}$, υπάρχει $\delta > 0$ τέτοιο ώστε για κάθε $x \in \mathbb{R}$ με $|x - x_{0}|< \delta$ έχουμε $|f(x)-f(x_{0})|<\epsilon \implies f(x) < 0$. Όμως απο την πυκνότητα των ρητών στο $\mathbb{R}$ έχουμε ότι υπάρχουν ρητοί οι οποιόι ικανοποιουν την σχέση $|x - x_{0}|< \delta$ και συνεπώς για αυτούς θα πρέπει $f(x) < 0$, πράγμα το οποίο είναι άτοπο.

Στα πλαίσια της παραπάνω απόδειξης, το συμπέρασμα βασίζεται στο οτι μπορούμε να ορίσουμε ένα $\epsilon > 0$ και να οδηγηθούμε σε άτοπο. Αν αντικαταστήσουμε το $\geq$ με $>$ τότε κάτι τέτοιο παύει να ισχύει. Γενικότερα αν $f(x) > 0$ για κάθε ρητό τότε θα μπορούσε να υπάρξει άρρητος με $f(x) = 0$.

## Θέμα 2

### Άσκηση 6, σελίδα 38

Η d ως μετρική στο $M$ ικανοποιεί τα παρακάτω:

1. $d(x, y) = 0 \iff x=y$
2. $d(x, y) = d(y, x)$
3. $d(x, y) \leq d(x, z) + d(z, y)$

Συνεπώς έχουμε τα εξής:

- $\rho: M \times M \rightarrow \mathbb{R}$ με $\rho(x, y)=\sqrt{d(x, y)}$

1. $\rho(x, y) = 0 \iff d(x, y) = 0 \iff x=y$
2. $\rho(x, y) = \sqrt{d(x, y)} = \sqrt{d(y, x)} = \rho(y, x)$
3. $\rho(x, y) = \sqrt{d(x, y)} \leq \sqrt{d(x, z) + d(z, y)} \leq \sqrt{d(x, z)} + \sqrt{d(z, y)} = \rho(x, z) + \rho(z, y)$

Άρα $\rho$ μετρική στο $M$.

- $\sigma: M \times M \rightarrow \mathbb{R}$ με $\sigma(x, y)=\frac{d(x, y)}{1 + d(x, y)} = F(d(x, y))$ όπου $F(t) = \frac{t}{t + 1}, t \geq 0$

Όμως για $t > 0$ έχουμε $F(t) = \frac{1}{1 + \frac{1}{t}}$ ενώ $F(0) = 0$. Συνεπώς η $F$ είναι αύξουσα για $t \geq 0$. Επίσης $F(s+t)=\frac{s+t}{1+s+t}=\frac{s}{1+s+t}+\frac{t}{1+s+t} \leqslant \frac{s}{1+s}+\frac{t}{1+t} =F(s)+F(t)$. Άρα $F(d(x, y)) \leq F(d(x, z) + d(z, y)) \leq F(d(x, z)) + F(d(z, y))$.

1. $\sigma(x, y) = 0 \iff \frac{d(x, y)}{1 + d(x, y)} = 0 \iff d(x, y) = 0 \iff x = y$
2. $\sigma(x, y) = \frac{d(x, y)}{1 + d(x, y)} = \frac{d(y, x)}{1 + d(y, x)} = \sigma(y, x)$
3. $\sigma(x, y) = F(d(x, y)) \leq F(d(x, z)) + F(d(z, y)) = \sigma(x, z) + \sigma(z, y)$

Άρα $\sigma$ μετρική στο $M$.

Όμως $\min \{a, 1\} \leq \min \{b, 1\}$ αν $0 \leq a \leq b$. Επίσης $\min \{a + b, 1\} \leq \min \{a, 1\} + \min \{b, 1\}$ αν $0 \leq a \leq b$.

- $\tau: M \times M \rightarrow \mathbb{R}$ με $\tau(x, y)=\min \{d(x, y), 1\}$

1. $\tau(x, y) = 0 \iff \min \{d(x, y), 1\} = 0 \iff d(x, y) = 0 \iff x=y$
2. $\tau(x, y) = \min \{d(x, y), 1\} = \min \{d(y, x), 1\} = \tau(y, x)$
2. $\tau(x, y) = \min \{d(x, y), 1\} \leq \min \{d(x, z), 1\} + \min \{d(z, y), 1\} = \tau(x, z) + \tau(z, y)$

Άρα $\tau$ μετρική στο $M$.

### Άσκηση 8, σελίδα 39

Απο τον ορισμό της μετρικής, ομοίως με την προηγούμενη άσκηση, προκύπτουν τα παρακάτω:

- $d_{1} + d_{2}$ είναι μετρική.
- $\max \{d_{1}, d_{2} \}$ είναι μετρική.
- $d^{2}$ είναι μετρική.

Αντίθετα η $d = \min \{d_{1}, d_{2} \}$ γενικά δεν είναι μετρική. Ένα αντιπαράδειγμα για $M = \mathbb{R}^{2}$ είναι το εξής:

$$d_{1}(x, y)=\sqrt{\left(x_{1}-y_{1}\right)^{2}+\frac{1}{100}\left(x_{2}-y_{2}\right)^{2}}$$

$$d_{2}(x, y)=\sqrt{\frac{1}{100}\left(x_{1}-y_{1}\right)^{2}+\left(x_{2}-y_{2}\right)^{2}}$$

Τότε $d(x, y) > d(x, z) + d(z, y)$ όπου $x=(1,0)$, $y=(0,1)$ και $z=(0,0)$.

## Θέμα 3

### Άσκηση 31, σελίδα 45

- $A = [0, 1] \subset \mathbb{R}$ και $B = [2, 3] \subset \mathbb{R}$. Τότε $diam(A) = 1$ και $diam(B) = 1$ ενώ $diam(A \cup B) = 3$.
- Έστω $x, y \in A \cup B$. Αν και τα δύο ανήκουν στο $A$ τότε $d(x, y) \leq diam(A)$. Αν και τα δύο ανήκουν στο $B$ τότε $d(x, y) \leq diam(B)$. Ας υποθέσουμε ότι $x \in A$ και $x \in B$. Έστω $z \in A \cap B$. Τότε απο την τριγωνική ανισότητα έχουμε:

  $$d(x, y) \leq d(x, z)+d(z, y) \leq d(A)+d(B)$$

  Συνεπώς $d(A \cup B) \leq d(A)+d(B)$.

## Θέμα 4

### Άσκηση 37, σελίδα 47

Υποθέτουμε ότι υπάρχει μια υπακολουθία $\left(x_{n_{k}}\right)$ της $\left(x_{n}\right)$ με $x_{n_{k}} \rightarrow x$. Έστω $\epsilon > 0$. Διαλέγουμε ένα $N$ τέτοιο ώστε $d\left(x_{n_{k}}, x\right)<\varepsilon$ και $d\left(x_{n}, x_{m}\right)<\varepsilon$ για $n, m > N$. Αφού $n > N$, έχουμε $n_{k} > n > N$ και συνεπώς:

$$d\left(x_{n}, x\right) \leq d\left(x_{n}, x_{n_{k}}\right)+d\left(x_{n_{k}}, x\right)<2 \varepsilon$$

Άρα $x_{n} \rightarrow x$.

### Άσκηση 42, σελίδα 48

Θα δείξουμε ότι οι μετρικές $d$ και $\rho$ είναι ισοδύναμες.

$d\left(x_{n}, x\right) \rightarrow 0 \iff (\forall \epsilon > 0)(\exists N: d(x_{n}, x) < \epsilon, \forall n > N) \iff$
$\iff (\forall \epsilon > 0)(\exists N: \sqrt{d(x_{n}, x)} < \epsilon, \forall n > N) \iff \rho\left(x_{n}, x\right) \rightarrow 0$

Ομοίως προκύπτει η ισοδυναμία για τις $\sigma$ και $\tau$ και την $d$.

## Θέμα 5

### Άσκηση 19, σελίδα 57

Έχουμε ότι $A \subset \bar{A}$ και συνεπώς $diam(A) \leq diam( \bar{A} )$.

Έστω $\epsilon > 0$. Θεωρούμε δύο σημεία $x, y \in \bar{A}$. Απο τον ορισμό του $\bar{A}$ υπάρχουν δύο σημεία $x', y' \in A$ τέτοια ώστε $d(x, x') < \epsilon$ και $d(y, y') < \epsilon$. Άρα:

$d(x, y) \leq d(x, x') + d(x', y') + d(y', y) \leq 2\epsilon + d(x', y') \leq 2\epsilon + diam(A)$

Έτσι έχουμε ότι $diam(\bar{A}) \leq 2\epsilon + diam(A)$ για μια αυθαίρετη τιμή του $\epsilon$.


Συνεπώς $diam(A) = diam( \bar{A} )$.

## Θέμα 6

### Άσκηση 26, σελίδα 57

Έχουμε τις εξής ισοδυναμίες:

$x \in \bar{A} \iff (\forall \epsilon > 0)(B(x, \epsilon) \cap A \neq \emptyset) \iff$
$\iff (\forall \epsilon > 0)(\exists a \in A: d(x, a)< \epsilon) \iff \inf_{a \in A} d(x, a) = 0 \iff d(X, A) = 0$

## Θέμα 7

### Άσκηση 35, σελίδα 58

Έστω $x$ οριακό σημείο του A'. Για $\epsilon > 0$ υπάρχει $y \in A'$ με $d(x, y) < \frac{\epsilon}{2}$.  Αφού $y \in A'$ υπάρχει $z \in A$ τέτοιο ώστε $0<d(y, z)<d(x, y)$. Απο την τριγωνική ανισότητα έχουμε $d(x, z) \leq d(x, y)+d(y, z)<\epsilon$. Άρα το $x$ είναι οριακό σημείο και του $A$ και συνπεώς $A'' \subset A'$. Άρα το $Α'$ είναι κλειστό.

### Άσκηση 36, σελίδα 58

## Θέμα 8

### Άσκηση 33, σελίδα 58

Υποθέτουμε ότι υπάρχει μια γειτονια $U = B_{\epsilon}(x)$ του $x$ τέτοια ώστε το $U \cap A = \{ a_{1}, \cdots, a_{k} \}$ για κάποιο πεπερασμένο $k$. Θεωρούμε το $B_{r}(x)$ με $r < \min \{ d(x, a_{1}), \cdots, d(x, a_{k})\}$. Τότε $B_{r}(x) \subset U$ με $a_{i} \notin B_{r}(x)$. Όμως $x$ είναι limit point και έτσι υπάρχει κάποιο $a \in A$ με $a \neq x$ το οποίο ανήκει στην $B_{r}(x)$. Άρα βρήκαμε ένα νέο σημείο για το $U \cap A$ το οποίο οδηγεί σε άτοπο.

## Θέμα 9

### Άσκηση 41, σελίδα 58

(a) Αν $x$ είναι οριακό σημείο του $A$ τότε $B_{\epsilon}(x) \cap A \neq \varnothing$ και $B_{\epsilon}(x) \cap A^{c} \neq \varnothing$ για κάθε $\epsilon > 0$. Ο ορισμός αυτός είναι ίδιος στην περίπτωση που το $x$ είναι οριακό σημείο του $A^{c}$. Άρα $bdry(A) = bdry(A^{c})$. 

