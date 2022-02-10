fn main() {
    // mut enables changing the value
    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);

    // non mutable but can be changed with shadowing
    let y = 5;
    println!("The value of Y is: {}", y);
    let y = 12;
    println!("The value of Y is: {}", y);
    const PI: f64 = 3.14159;

    println!("The value of PI is: {}", PI);
}

fn ownership() {
    // un ámbito o scope existe dentro de {}
    {
        // x no existe aún
        let x = String::from("Hello"); // x ya existe y es váldio
                                       // realizar cualquier acción con x
    } // x ya no existe, no es valido, terminó su ámbito (scope)
}

fn calls_function() {
    let value = String::from("Hello, world");
    take_ownership(value);
    // ya no es dueña de la variable
    // println!("{}", value);
}

fn take_ownership(some_variable: String) {
    //  cuando la variable entra en una función, esta última
    //  es propietaria de tal variuable
    println!("{}", some_variable);
}

fn give_ownership() -> String {
    // al regresar un valor, ese valor ahora es propiedad del
    // que llamó a esta funcion
    let given = String::from("Hola, mundo");
    given
}

// esta funcion no se apropia de la variable
// & hace que solo se referencie a x
fn calculate_length(x: &String) -> usize {
    // x es inmutable, sólo se tiene acceso a sus propiedades
    let length = x.len();
    length
}

// la keyword mut hace que una referencia sea mutable
fn mutable_ref(some_string: &mut String){
    some_string.push_str(", World!");
}
