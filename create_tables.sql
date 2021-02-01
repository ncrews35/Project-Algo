CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL,
    name TEXT NOT NULL,
    exchange TEXT NOT NULL,
    is_shortable BOOLEAN NOT NULL
);

CREATE TABLE mention (
    stock_id INTEGER NOT NULL,
    dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    message TEXT NOT NULL, 
    source TEXT NOT NULL,
    url TEXT NOT NULL,
    PRIMARY KEY (stock_id, dt),
    CONSTRAINT fk_mention_stock FOREIGN KEY (stock_id) REFERENCES stock (id)
);

CREATE INDEX ON mention (stock_id, dt DESC);
SELECT create_hypertable('mention', 'dt');

CREATE TABLE stock_price (
    stock_id INTEGER NOT NULL,
    dt TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    open NUMERIC NOT NULL,
    high NUMERIC NOT NULL,
    low NUMERIC NOT NULL,
    close NUMERIC NOT NULL,
    volume NUMERIC NOT NULL,
    PRIMARY KEY (stock_id, dt),
    CONSTRAINT dk_stock FOREIGN KEY (stock_id) REFERENCES stock (id)
);



CREATE INDEX ON stock_price (stock_id, dt DESC);
SELECT create_hypertable('stock_price', 'dt');


select count(*) as num_mentions, stock_id, symbol
from mention join stock on stock.id = mention.stock_id
group by stock_id, symbol
order by num_mentions DESC;
