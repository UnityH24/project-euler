fact :: Integer -> Integer
fact n
 | n <= 1 = 1
 | otherwise = n * fact (n - 1)

sum_digits :: Integer -> Integer
sum_digits 0 = 0
sum_digits n = (mod n 10) + sum_digits (n `div` 10)

main :: IO()
main = do
    print (sum_digits (fact 100))
