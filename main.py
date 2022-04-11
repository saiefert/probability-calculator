import prob_calculator

def main():
    prob_calculator.random.seed(95)
    hat = prob_calculator.Hat(red=5,blue=2)
    print(hat.draw(2))
    probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
    print("Probability:", probability)
    print(len(hat.contents))

if __name__ == "__main__":
    main()
