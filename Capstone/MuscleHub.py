{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone Project 1: MuscleHub AB Test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Get started with SQL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Like most businesses, Janet keeps her data in a SQL database.  Normally, you'd download the data from her database to a csv file, and then load it into a Jupyter Notebook using Pandas.\n",
    "\n",
    "For this project, you'll have to access SQL in a slightly different way.  You'll be using a special Codecademy library that lets you type SQL queries directly into this Jupyter notebook.  You'll have pass each SQL query as an argument to a function called `sql_query`.  Each query will return a Pandas DataFrame.  Here's an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# This import only needs to happen once, at the beginning of the notebook\n",
    "from codecademySQL import sql_query"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Here's an example of a query that just displays some data\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Here's an example where we save the data to a DataFrame\n",
    "df = sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Get your dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's get started!\n",
    "\n",
    "Janet of MuscleHub has a SQLite database, which contains several tables that will be helpful to you in this investigation:\n",
    "- `visits` contains information about potential gym customers who have visited MuscleHub\n",
    "- `fitness_tests` contains information about potential customers in \"Group A\", who were given a fitness test\n",
    "- `applications` contains information about any potential customers (both \"Group A\" and \"Group B\") who filled out an application.  Not everyone in `visits` will have filled out an application.\n",
    "- `purchases` contains information about customers who purchased a membership to MuscleHub.\n",
    "\n",
    "Use the space below to examine each table."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>visit_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Karen</td>\n",
       "      <td>Manning</td>\n",
       "      <td>Karen.Manning@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Annette</td>\n",
       "      <td>Boone</td>\n",
       "      <td>AB9982@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Salvador</td>\n",
       "      <td>Merritt</td>\n",
       "      <td>SalvadorMerritt12@outlook.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Martha</td>\n",
       "      <td>Maxwell</td>\n",
       "      <td>Martha.Maxwell@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Andre</td>\n",
       "      <td>Mayer</td>\n",
       "      <td>AndreMayer90@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>5-1-17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                          email  gender  \\\n",
       "0      0      Karen   Manning        Karen.Manning@gmail.com  female   \n",
       "1      1    Annette     Boone               AB9982@gmail.com  female   \n",
       "2      2   Salvador   Merritt  SalvadorMerritt12@outlook.com    male   \n",
       "3      3     Martha   Maxwell       Martha.Maxwell@gmail.com  female   \n",
       "4      4      Andre     Mayer         AndreMayer90@gmail.com    male   \n",
       "\n",
       "  visit_date  \n",
       "0     5-1-17  \n",
       "1     5-1-17  \n",
       "2     5-1-17  \n",
       "3     5-1-17  \n",
       "4     5-1-17  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql_query('''\n",
    "SELECT *\n",
    "FROM visits\n",
    "LIMIT 5\n",
    "''')\n",
    "# Examine visits here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>fitness_test_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Kim</td>\n",
       "      <td>Walter</td>\n",
       "      <td>KimWalter58@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-03</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Tom</td>\n",
       "      <td>Webster</td>\n",
       "      <td>TW3857@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Marcus</td>\n",
       "      <td>Bauer</td>\n",
       "      <td>Marcus.Bauer@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Best</td>\n",
       "      <td>RB6305@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Carrie</td>\n",
       "      <td>Francis</td>\n",
       "      <td>CF1896@hotmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-07-05</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                   email  gender  \\\n",
       "0      0        Kim    Walter   KimWalter58@gmail.com  female   \n",
       "1      1        Tom   Webster        TW3857@gmail.com    male   \n",
       "2      2     Marcus     Bauer  Marcus.Bauer@gmail.com    male   \n",
       "3      3    Roberta      Best      RB6305@hotmail.com  female   \n",
       "4      4     Carrie   Francis      CF1896@hotmail.com  female   \n",
       "\n",
       "  fitness_test_date  \n",
       "0        2017-07-03  \n",
       "1        2017-07-02  \n",
       "2        2017-07-01  \n",
       "3        2017-07-02  \n",
       "4        2017-07-05  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Examine fitness_tests here\n",
    "sql_query('''\n",
    "SELECT *\n",
    "FROM fitness_tests\n",
    "LIMIT 5\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>application_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Agnes</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>AgnesAcevedo1@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender  \\\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male   \n",
       "1      1      Agnes   Acevedo  AgnesAcevedo1@gmail.com  female   \n",
       "2      2    Roberta   Acevedo         RA8063@gmail.com  female   \n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male   \n",
       "4      4     Vernon    Acosta    VAcosta1975@gmail.com    male   \n",
       "\n",
       "  application_date  \n",
       "0       2017-08-12  \n",
       "1       2017-09-29  \n",
       "2       2017-09-15  \n",
       "3       2017-07-26  \n",
       "4       2017-07-14  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql_query('''\n",
    "SELECT *\n",
    "FROM applications\n",
    "LIMIT 5\n",
    "''')\n",
    "# Examine applications here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "      <th>gender</th>\n",
       "      <th>purchase_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Roy</td>\n",
       "      <td>Abbott</td>\n",
       "      <td>RoyAbbott32@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-08-18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Roberta</td>\n",
       "      <td>Acevedo</td>\n",
       "      <td>RA8063@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-09-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>Vernon</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>VAcosta1975@gmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Darren</td>\n",
       "      <td>Acosta</td>\n",
       "      <td>DAcosta1996@hotmail.com</td>\n",
       "      <td>male</td>\n",
       "      <td>2017-07-27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Dawn</td>\n",
       "      <td>Adkins</td>\n",
       "      <td>Dawn.Adkins@gmail.com</td>\n",
       "      <td>female</td>\n",
       "      <td>2017-08-24</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   index first_name last_name                    email  gender purchase_date\n",
       "0      0        Roy    Abbott    RoyAbbott32@gmail.com    male    2017-08-18\n",
       "1      1    Roberta   Acevedo         RA8063@gmail.com  female    2017-09-16\n",
       "2      2     Vernon    Acosta    VAcosta1975@gmail.com    male    2017-07-20\n",
       "3      3     Darren    Acosta  DAcosta1996@hotmail.com    male    2017-07-27\n",
       "4      4       Dawn    Adkins    Dawn.Adkins@gmail.com  female    2017-08-24"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sql_query('''\n",
    "SELECT *\n",
    "FROM purchases\n",
    "LIMIT 5\n",
    "''')\n",
    "\n",
    "# Examine purchases here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to download a giant DataFrame containing all of this data.  You'll need to write a query that does the following things:\n",
    "\n",
    "1. Not all visits in  `visits` occurred during the A/B test.  You'll only want to pull data where `visit_date` is on or after `7-1-17`.\n",
    "\n",
    "2. You'll want to perform a series of `LEFT JOIN` commands to combine the four tables that we care about.  You'll need to perform the joins on `first_name`, `last_name`, and `email`.  Pull the following columns:\n",
    "\n",
    "\n",
    "- `visits.first_name`\n",
    "- `visits.last_name`\n",
    "- `visits.gender`\n",
    "- `visits.email`\n",
    "- `visits.visit_date`\n",
    "- `fitness_tests.fitness_test_date`\n",
    "- `applications.application_date`\n",
    "- `purchases.purchase_date`\n",
    "\n",
    "Save the result of this query to a variable called `df`.\n",
    "\n",
    "Hint: your result should have 5004 rows.  Does it?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = sql_query(\n",
    "'''\n",
    "SELECT visits.first_name,visits.last_name,visits.gender,visits.email,visits.visit_date,fitness_tests.fitness_test_date,applications.application_date,purchases.purchase_date\n",
    "FROM visits\n",
    "LEFT JOIN fitness_tests\n",
    "ON visits.first_name = fitness_tests.first_name AND visits.last_name = fitness_tests.last_name AND visits.email = fitness_tests.email\n",
    "LEFT JOIN applications\n",
    "ON visits.first_name = applications.first_name AND visits.last_name = applications.last_name AND visits.email = applications.email\n",
    "LEFT JOIN  purchases\n",
    "ON visits.first_name = purchases.first_name AND visits.last_name = purchases.last_name AND visits.email = purchases.email\n",
    "WHERE visits.visit_date >= \"7-1-17\"\n",
    "''')\n",
    "\n",
    "#df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Investigate the A and B groups"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have some data to work with! Import the following modules so that we can start doing analysis:\n",
    "- `import pandas as pd`\n",
    "- `from matplotlib import pyplot as plt`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to add some columns to `df` to help us with our analysis.\n",
    "\n",
    "Start by adding a column called `ab_test_group`.  It should be `A` if `fitness_test_date` is not `None`, and `B` if `fitness_test_date` is `None`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['ab_test_group'] = df.fitness_test_date.apply(lambda x: 'A' if pd.notnull(x) else 'B')\n",
    "\n",
    "#df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's do a quick sanity check that Janet split her visitors such that about half are in A and half are in B.\n",
    "\n",
    "Start by using `groupby` to count how many users are in each `ab_test_group`.  Save the results to `ab_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>first_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>2504</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>2500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  ab_test_group  first_name\n",
       "0             A        2504\n",
       "1             B        2500"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ab_counts = df.groupby('ab_test_group').first_name.count().reset_index()\n",
    "\n",
    "ab_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'll want to include this information in our presentation.  Let's create a pie cart using `plt.pie`.  Make sure to include:\n",
    "- Use `plt.axis('equal')` so that your pie chart looks nice\n",
    "- Add a legend labeling `A` and `B`\n",
    "- Use `autopct` to label the percentage of each group\n",
    "- Save your figure as `ab_test_pie_chart.png`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "\n",
    "legend_titles = [\"A Group\", \"B Group\"]\n",
    "\n",
    "plt.pie(ab_counts.first_name, autopct='%0.2f%%')\n",
    "plt.axis('equal')\n",
    "plt.legend(legend_titles)\n",
    "plt.savefig('ab_test_pie_chart.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who picks up an application?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recall that the sign-up process for MuscleHub has several steps:\n",
    "1. Take a fitness test with a personal trainer (only Group A)\n",
    "2. Fill out an application for the gym\n",
    "3. Send in their payment for their first month's membership\n",
    "\n",
    "Let's examine how many people make it to Step 2, filling out an application.\n",
    "\n",
    "Start by creating a new column in `df` called `is_application` which is `Application` if `application_date` is not `None` and `No Application`, otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['is_application'] = df.application_date.apply(lambda x: 'Application' if pd.notnull(x) else 'No Application')\n",
    "\n",
    "#df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, using `groupby`, count how many people from Group A and Group B either do or don't pick up an application.  You'll want to group by `ab_test_group` and `is_application`.  Save this new DataFrame as `app_counts`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>first_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Application</td>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Application</td>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>No Application</td>\n",
       "      <td>A</td>\n",
       "      <td>2254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>No Application</td>\n",
       "      <td>B</td>\n",
       "      <td>2175</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   is_application ab_test_group  first_name\n",
       "0     Application             A         250\n",
       "1     Application             B         325\n",
       "2  No Application             A        2254\n",
       "3  No Application             B        2175"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_counts = df.groupby(['is_application','ab_test_group']).first_name.count().reset_index()\n",
    "\n",
    "app_counts"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're going to want to calculate the percent of people in each group who complete an application.  It's going to be much easier to do this if we pivot `app_counts` such that:\n",
    "- The `index` is `ab_test_group`\n",
    "- The `columns` are `is_application`\n",
    "Perform this pivot and save it to the variable `app_pivot`.  Remember to call `reset_index()` at the end of the pivot!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application\n",
       "0                          A          250            2254\n",
       "1                          B          325            2175"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_counts_pivot = app_counts.pivot(columns='is_application',index='ab_test_group', values='first_name').reset_index()\n",
    "\n",
    "app_counts_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a new column called `Total`, which is the sum of `Application` and `No Application`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "      <th>Total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "      <td>2504</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "      <td>2500</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application  Total\n",
       "0                          A          250            2254   2504\n",
       "1                          B          325            2175   2500"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_counts_pivot['Total'] = app_counts_pivot['Application'] + app_counts_pivot['No Application']\n",
    "\n",
    "app_counts_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate another column called `Percent with Application`, which is equal to `Application` divided by `Total`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_application</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Application</th>\n",
       "      <th>No Application</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent with Application</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>250</td>\n",
       "      <td>2254</td>\n",
       "      <td>2504</td>\n",
       "      <td>0.09984</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>325</td>\n",
       "      <td>2175</td>\n",
       "      <td>2500</td>\n",
       "      <td>0.13000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_application ab_test_group  Application  No Application  Total  \\\n",
       "0                          A          250            2254   2504   \n",
       "1                          B          325            2175   2500   \n",
       "\n",
       "is_application  Percent with Application  \n",
       "0                                0.09984  \n",
       "1                                0.13000  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "app_counts_pivot['Percent with Application'] = app_counts_pivot['Application'] / app_counts_pivot['Total']\n",
    "\n",
    "app_counts_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like more people from Group B turned in an application.  Why might that be?\n",
    "\n",
    "We need to know if this difference is statistically significant.\n",
    "\n",
    "Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10.893961295282612,\n",
       " 0.0009647827600722304,\n",
       " 1L,\n",
       " array([[ 287.72981615, 2216.27018385],\n",
       "        [ 287.27018385, 2212.72981615]]))"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency\n",
    "\n",
    "# Group  |     Application  |  No App\n",
    "#   A    |        250       |   2254\n",
    "#   B    |        325       |   2175\n",
    "\n",
    "x = [[250, 2254],\n",
    "    [325, 2175]]\n",
    "\n",
    "chi2_contingency(x)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Who purchases a membership?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Of those who picked up an application, how many purchased a membership?\n",
    "\n",
    "Let's begin by adding a column to `df` called `is_member` which is `Member` if `purchase_date` is not `None`, and `Not Member` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['is_member'] = df.purchase_date.apply(lambda x: 'Member' if pd.notnull(x) else 'Not Member')\n",
    "\n",
    "#print df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, let's create a DataFrame called `just_apps` the contains only people who picked up an application."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "just_apps = df[df.is_application == 'Application']\n",
    "\n",
    "#print(just_apps)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now, let's do a `groupby` to find out how many people in `just_apps` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_member</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Member</th>\n",
       "      <th>Not Member</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent Purchase</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>200</td>\n",
       "      <td>50</td>\n",
       "      <td>250</td>\n",
       "      <td>0.800000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>250</td>\n",
       "      <td>75</td>\n",
       "      <td>325</td>\n",
       "      <td>0.769231</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
       "0                     A     200          50    250          0.800000\n",
       "1                     B     250          75    325          0.769231"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "member_count = just_apps.groupby(['is_member','ab_test_group'])\\\n",
    "                .first_name.count().reset_index()\n",
    "#print(just_apps)\n",
    "\n",
    "member_pivot  = member_count.pivot(columns='is_member',index='ab_test_group', values='first_name').reset_index()\n",
    "member_pivot['Total'] = member_pivot['Member'] + member_pivot['Not Member']\n",
    "member_pivot['Percent Purchase'] = member_pivot['Member'] / member_pivot['Total']\n",
    "\n",
    "\n",
    "member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like people who took the fitness test were more likely to purchase a membership **if** they picked up an application.  Why might that be?\n",
    "\n",
    "Just like before, we need to know if this difference is statistically significant.  Choose a hypothesis tests, import it from `scipy` and perform it.  Be sure to note the p-value.\n",
    "Is this result significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.615869230769231,\n",
       " 0.43258646051083327,\n",
       " 1L,\n",
       " array([[195.65217391,  54.34782609],\n",
       "        [254.34782609,  70.65217391]]))"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency\n",
    "\n",
    "# Group  |     Member       |  Not Member\n",
    "#   A    |        200       |   50\n",
    "#   B    |        250       |   75\n",
    "\n",
    "x = [[200, 50],\n",
    "    [250, 75]]\n",
    "\n",
    "chi2_contingency(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, we looked at what percent of people **who picked up applications** purchased memberships.  What we really care about is what percentage of **all visitors** purchased memberships.  Return to `df` and do a `groupby` to find out how many people in `df` are and aren't members from each group.  Follow the same process that we did in Step 4, including pivoting the data.  You should end up with a DataFrame that looks like this:\n",
    "\n",
    "|is_member|ab_test_group|Member|Not Member|Total|Percent Purchase|\n",
    "|-|-|-|-|-|-|\n",
    "|0|A|?|?|?|?|\n",
    "|1|B|?|?|?|?|\n",
    "\n",
    "Save your final DataFrame as `final_member_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_member</th>\n",
       "      <th>ab_test_group</th>\n",
       "      <th>Member</th>\n",
       "      <th>Not Member</th>\n",
       "      <th>Total</th>\n",
       "      <th>Percent Purchase</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>200</td>\n",
       "      <td>2304</td>\n",
       "      <td>2504</td>\n",
       "      <td>0.079872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>250</td>\n",
       "      <td>2250</td>\n",
       "      <td>2500</td>\n",
       "      <td>0.100000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_member ab_test_group  Member  Not Member  Total  Percent Purchase\n",
       "0                     A     200        2304   2504          0.079872\n",
       "1                     B     250        2250   2500          0.100000"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_member = df.groupby(['is_member','ab_test_group']).first_name.count().reset_index()\n",
    "#print(final_member)\n",
    "\n",
    "final_member_pivot  = final_member.pivot(columns='is_member',index='ab_test_group', values='first_name').reset_index()\n",
    "final_member_pivot['Total'] = final_member_pivot['Member'] + final_member_pivot['Not Member']\n",
    "final_member_pivot['Percent Purchase'] = final_member_pivot['Member'] / final_member_pivot['Total']\n",
    "\n",
    "final_member_pivot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Previously, when we only considered people who had **already picked up an application**, we saw that there was no significant difference in membership between Group A and Group B.\n",
    "\n",
    "Now, when we consider all people who **visit MuscleHub**, we see that there might be a significant different in memberships between Group A and Group B.  Perform a significance test and check."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5.949182292591156,\n",
       " 0.014724114645783203,\n",
       " 1L,\n",
       " array([[ 225.17985612, 2278.82014388],\n",
       "        [ 224.82014388, 2275.17985612]]))"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy.stats import chi2_contingency\n",
    "\n",
    "# Group  |     Member       |  Not Member\n",
    "#   A    |        200       |   2304\n",
    "#   B    |        250       |   2250\n",
    "\n",
    "x = [[200, 2304],\n",
    "    [250, 2250]]\n",
    "\n",
    "chi2_contingency(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Summarize the acquisition funel with a chart"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We'd like to make a bar chart for Janet that shows the difference between Group A (people who were given the fitness test) and Group B (people who were not given the fitness test) at each state of the process:\n",
    "- Percent of visitors who apply\n",
    "- Percent of applicants who purchase a membership\n",
    "- Percent of visitors who purchase a membership\n",
    "\n",
    "Create one plot for **each** of the three sets of percentages that you calculated in `app_pivot`, `member_pivot` and `final_member_pivot`.  Each plot should:\n",
    "- Label the two bars as `Fitness Test` and `No Fitness Test`\n",
    "- Make sure that the y-axis ticks are expressed as percents (i.e., `5%`)\n",
    "- Have a title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.bar(range(len(app_counts_pivot.ab_test_group)), app_counts_pivot['Percent with Application'])\n",
    "ax1 = plt.subplot()\n",
    "ax1.set_xticks(range(len(app_counts_pivot.ab_test_group)))\n",
    "ax1.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "ax1.set_yticks([0, 0.05, 0.1, 0.15, 0.20])\n",
    "ax1.set_yticklabels(['0%','5%','10%','15%','20%'])\n",
    "plt.title('Visitors Who Apply for Membership')\n",
    "plt.ylabel('Percentage of Customers')\n",
    "plt.savefig('percentage_visit_apply.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.bar(range(len(member_pivot.ab_test_group)), member_pivot['Percent Purchase'])\n",
    "ax2 = plt.subplot()\n",
    "ax2.set_xticks(range(len(final_member_pivot.ab_test_group)))\n",
    "ax2.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "ax2.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])\n",
    "ax2.set_yticklabels(['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100'])\n",
    "plt.title('Applicants who Purchase a Membership')\n",
    "plt.ylabel('Percentage of Customers')\n",
    "plt.savefig('percentage_apply_purchase.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.bar(range(len(final_member_pivot.ab_test_group)), final_member_pivot['Percent Purchase'])\n",
    "ax3 = plt.subplot()\n",
    "ax3.set_xticks(range(len(final_member_pivot.ab_test_group)))\n",
    "ax3.set_xticklabels(['Fitness Test','No Fitness Test'])\n",
    "ax3.set_yticks([0, 0.05, 0.1, 0.15, .2])\n",
    "ax3.set_yticklabels(['0%','5%','10%','15%','20%'])\n",
    "plt.title('Visitors who Purchase a Membership')\n",
    "plt.ylabel('Percentage of Customers')\n",
    "plt.savefig('percentage_visit_purchase.png')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
