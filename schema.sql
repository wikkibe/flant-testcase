drop table if exists hit;
create table hit (
    id serial primary key,
    url varchar(1024) not null,
    ts timestamp not null default now());

create or replace function pgq_new_hit() returns trigger as $$
	begin
		perform pgq.insert_event('flant_queue', 'hit', new.url::text);
		return new;
	end;
$$ language plpgsql;

drop trigger if exists pgq_new_hit on hit;
create trigger pgq_new_hit after insert on hit for each row execute procedure pgq_new_hit();


drop table if exists stat;
create table stat (
    url varchar(1024) primary key,
    hits int not null);