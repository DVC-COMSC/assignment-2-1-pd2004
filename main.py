def main():
    male = int(input("Male count: "))
    female = int(input("Female count: "))

    total = male + female
    
    m_perc = (male / total) * 100.0
    f_perc = (female / total) * 100.0

    return m_perc, f_perc


if __name__ == '__main__':
    main()
