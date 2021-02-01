CREATE TABLE stock {
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    name TEXT NOT NULL,
    exchange TEXT NOT NULL,
    is_etf BOOLEAN NOT NULL
};

CREATE TABLE mention {
    stock_id INTEGER,
    dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    message TEXT NOT NULL, 
    source TEXT NOT NULL, -- wsb, twitter, ect.
    url TEXT NOT NULL,
    PRIMARY KEY (stock_id, dt):
    CONSTRAINT fk_mention_stock DOREIGN KEY (stock_id) REFERENCES stock (id)
};

