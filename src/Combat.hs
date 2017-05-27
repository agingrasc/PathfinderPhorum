module Combat(
              Character(..),
              executeFullCombat)
              where

data Character = Character { hp :: Int,
                             ac :: Int,
                             damage :: Int,
                             attackBonus :: Int,
                             name :: String
                           } deriving (Show)

executeFullCombat :: Character -> Character -> [(String, Int)]
executeFullCombat attacker defender
    | hp attacker <= 0 = []
    | otherwise = (name defender, executeAttack attacker defender) : executeFullCombat (updateHp defender resultHp) attacker
    where resultHp = executeAttack attacker defender

executeAttack :: Character -> Character -> Int
executeAttack attacker defender
    | connected = resultHp
    | otherwise = hp defender
    where connected = resolveHit (attackBonus attacker) (ac defender)
          resultHp = hp defender - damage attacker

resolveHit :: Int -> Int -> Bool
resolveHit attackBonus defense = defense < attackBonus

updateHp :: Character -> Int -> Character
updateHp character remaining = character {hp = remaining}
