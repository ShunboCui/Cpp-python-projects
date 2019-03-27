/**
 * \file CardTypes.h
 * \author Shunbo Cui
 * \brief Defines every types needed in the project
 */
#ifndef A3_CARD_TYPES_H_
#define A3_CARD_TYPES_H_

/**
 * \brief Describes the rank of a card.
 */
typedef unsigned short int RankT;

/**
 * \brief RankT for an Ace.
 */
#define ACE    1

/**
 * \brief RankT for an Jack.
 */
#define JACK   11

/**
 * \brief RankT for a Queen.
 */
#define QUEEN  12

/**
 * \brief RankT for a King.
 */
#define KING   13

 /**
  * \brief Total number of all cards.
  */
#define TOTAL_CARDS   104

  /**
   * \brief The suit of cards.
   */
enum SuitT {N, S, E, W};

/**
 * \brief Four card containers on the gameboard.
 */
enum CategoryT {Tableau, Foundation, Deck, Waste};

/**
 * \brief The two properties of every eard.
 */
typedef struct
{
SuitT s;
RankT r;
}CardT;

#endif
