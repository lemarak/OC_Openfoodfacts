SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

-- Table categories

DROP TABLE IF EXISTS oc_openfoodfacts.categories ;

CREATE TABLE IF NOT EXISTS oc_openfoodfacts.categories (
  id_category VARCHAR(255) NOT NULL,
  name VARCHAR(100) NOT NULL,
  products INT NULL,
  url VARCHAR(255) NULL,
  visible TINYINT(1) NULL DEFAULT 0,
  PRIMARY KEY (id_category))
ENGINE = InnoDB;

-- Table products

DROP TABLE IF EXISTS oc_openfoodfacts.products ;

CREATE TABLE IF NOT EXISTS oc_openfoodfacts.products (
  id_product VARCHAR(15) NOT NULL,
  product_name_fr VARCHAR(150) NOT NULL,
  nutriscore_score INT NULL,
  nutriscore_grade CHAR(1) NULL,
  stores VARCHAR(255) NULL,
  generic_name_fr MEDIUMTEXT NULL,
  brands VARCHAR(100) NULL,
  PRIMARY KEY (id_product))
ENGINE = InnoDB;


-- Table cat_prod

DROP TABLE IF EXISTS oc_openfoodfacts.cat_prod ;

CREATE TABLE IF NOT EXISTS oc_openfoodfacts.cat_prod (
  id_category VARCHAR(150) NOT NULL,
  id_product VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_category, id_product),
  CONSTRAINT fk_category
    FOREIGN KEY (id_category)
    REFERENCES oc_openfoodfacts.categories (id_category)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_product
    FOREIGN KEY (id_product)
    REFERENCES oc_openfoodfacts.products (id_product)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX fk_product_idx ON oc_openfoodfacts.cat_prod (id_product ASC) INVISIBLE;

CREATE INDEX fk_category_idx ON oc_openfoodfacts.cat_prod (id_category ASC) VISIBLE;

-- Table users

DROP TABLE IF EXISTS oc_openfoodfacts.users ;

CREATE TABLE IF NOT EXISTS oc_openfoodfacts.users (
  id_user INT NOT NULL AUTO_INCREMENT,
  login VARCHAR(20) NOT NULL,
  name VARCHAR(50) NOT NULL,
  password BINARY(60) NULL,
  PRIMARY KEY (id_user))
ENGINE = InnoDB;

-- insert one user by default
INSERT INTO oc_openfoodfacts.users (login, name, password) VALUES ('test', 'Utilisateur test', '$2y$10$O7LoyXL3mCtLZp5.Lfn4ReiKPhtw5.pp6J11wNZONh.YgS9eV1TA.');


-- Table favorites

DROP TABLE IF EXISTS oc_openfoodfacts.favorites ;

CREATE TABLE IF NOT EXISTS oc_openfoodfacts.favorites (
  id_user INT NOT NULL,
  id_product VARCHAR(15) NOT NULL,
  PRIMARY KEY (id_user, id_product),
  CONSTRAINT fk_user
    FOREIGN KEY (id_user)
    REFERENCES oc_openfoodfacts.users (id_user)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_favorite_product
    FOREIGN KEY (id_product)
    REFERENCES oc_openfoodfacts.products (id_product)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX fk_idx_user ON oc_openfoodfacts.favorites (id_user ASC);

CREATE INDEX fk_idx_product ON oc_openfoodfacts.favorites (id_product ASC);

SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
