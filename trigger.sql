use hospital;
DELIMITER //
create trigger prevent before insert on hospital.appointment for each row 
begin
	declare existing_count int;
    select count(*) into existing_count
    from hospital.appointment
    where p_id=new.p_id and doctor_id=new.doctor_id;
    if existing_count>0 then
    signal sqlstate '45000'
    set message_text="You cannot assign a appointment once again";
    
end if;
end;
// 
DELIMITER ;