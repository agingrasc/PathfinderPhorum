data Character = Character { hp :: Int,
                             ac :: Int,
                             damage :: Int,
                             hit :: Int,
                             name :: String
                           } deriving (Show)


executeAttack :: Character -> Character -> Int
executeAttack attacker defender
    | connected = resultHp
    | otherwise = hp defender
    where connected = resolveHit (ac defender) (hit attacker)
          resultHp = hp defender - damage attacker

attackTillDead :: Character -> Character -> [(Character, Int)]
attackTillDead attacker defender
    | hp attacker <= 0 = []
    | otherwise = (defender, executeAttack attacker defender) : attackTillDead (updateHp defender resultHp) attacker
    where resultHp = executeAttack attacker defender

resolveHit :: Int -> Int -> Bool
resolveHit defense hit = defense < hit

updateHp :: Character -> Int -> Character
updateHp character remaining = character {hp = remaining}
