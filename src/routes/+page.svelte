<script lang='ts'>
    import { faker } from '@faker-js/faker';
    import Navbar from "/Users/alvar/dev/callopi/src/components/Navbar.svelte";
    import InfoSection from "/Users/alvar/dev/callopi/src/components/InfoSection.svelte";

    let links = [
        {text: 'Home', url: 'www.google.com'},
        {text: 'Transaction', url: '/Transaction/+page.svelte'}
    ];

    let product = {
        name: faker.commerce.product(),
        description: faker.commerce.productDescription(),
        price: faker.commerce.price()
    };

    
</script>

<Navbar {links} />


    <div>
        <!-- info side -->
        <section class="left">
            <InfoSection {product}/>
        </section>
        <!-- main body -->
        <section class="right">
            
        </section>
    </div>