// Simple Super Mario Bros Style Platformer
console.log('Game script loaded');

// Check if Phaser is available
if (typeof Phaser === 'undefined') {
    console.error('Phaser not loaded!');
    document.getElementById('game').innerHTML = '<h2 style="color: red;">Error: Phaser.js failed to load</h2>';
} else {
    console.log('Phaser loaded successfully!');
    
    // Game variables
    let player;
    let platforms;
    let coins;
    let cursors;
    let score = 0;
    let scoreText;
    
    // Game config
    const config = {
        type: Phaser.AUTO,
        width: 800,
        height: 600,
        parent: 'game',
        physics: {
            default: 'arcade',
            arcade: {
                gravity: { y: 300 },
                debug: false
            }
        },
        scene: {
            preload: preload,
            create: create,
            update: update
        }
    };
    
    // Start the game
    const game = new Phaser.Game(config);
    
    function preload() {
        console.log('Preload called');
    }
    
    function create() {
        console.log('Create called');
        
        // Background
        this.add.rectangle(400, 300, 800, 600, 0x87CEEB);
        
        // Create platforms
        platforms = this.physics.add.staticGroup();
        
        // Ground platform
        const ground = this.add.graphics();
        ground.fillStyle(0x8B4513);
        ground.fillRect(0, 0, 200, 32);
        const groundTexture = ground.generateTexture('ground', 200, 32);
        platforms.create(400, 568, 'ground').setScale(2, 1).refreshBody();
        
        // Floating platforms
        const platform1 = this.add.graphics();
        platform1.fillStyle(0x8B4513);
        platform1.fillRect(0, 0, 100, 32);
        const platform1Texture = platform1.generateTexture('platform1', 100, 32);
        platforms.create(600, 400, 'platform1').refreshBody();
        
        const platform2 = this.add.graphics();
        platform2.fillStyle(0x8B4513);
        platform2.fillRect(0, 0, 100, 32);
        const platform2Texture = platform2.generateTexture('platform2', 100, 32);
        platforms.create(200, 300, 'platform2').refreshBody();
        
        // Create coins
        coins = this.physics.add.group();
        
        // Create coin graphics
        const coinGraphics = this.add.graphics();
        coinGraphics.fillStyle(0xffd700); // Gold color
        coinGraphics.fillCircle(16, 16, 16);
        const coinTexture = coinGraphics.generateTexture('coin', 32, 32);
        
        // Create coin sprites
        for (let i = 0; i < 8; i++) {
            const coin = coins.create(Phaser.Math.Between(50, 750), Phaser.Math.Between(100, 500), 'coin');
            coin.setBounce(0.7);
            coin.setCollideWorldBounds(true);
            coin.setVelocity(Phaser.Math.Between(-100, 100), Phaser.Math.Between(-100, 100));
        }
        
        // Create player
        const playerGraphics = this.add.graphics();
        playerGraphics.fillStyle(0xff0000);
        playerGraphics.fillRect(0, 0, 32, 32);
        const playerTexture = playerGraphics.generateTexture('player', 32, 32);
        
        player = this.physics.add.sprite(100, 450, 'player');
        player.setBounce(0.2);
        player.setCollideWorldBounds(true);
        
        // Collision
        this.physics.add.collider(player, platforms);
        this.physics.add.collider(coins, platforms);
        
        // Player-coin collision
        this.physics.add.overlap(player, coins, collectCoin, null, this);
        
        // Controls
        cursors = this.input.keyboard.createCursorKeys();
        
        // Score
        scoreText = this.add.text(16, 16, 'Score: 0', {
            fontSize: '32px',
            fill: '#000'
        });
        
        console.log('Game created successfully!');
    }
    
    function update() {
        // Movement
        if (cursors.left.isDown) {
            player.setVelocityX(-160);
        } else if (cursors.right.isDown) {
            player.setVelocityX(160);
        } else {
            player.setVelocityX(0);
        }
        
        // Jumping
        if (cursors.up.isDown && player.body.touching.down) {
            player.setVelocityY(-330);
        }
    }
    
    function collectCoin(player, coin) {
        coin.destroy();
        score += 10;
        scoreText.setText('Score: ' + score);
        
        // Check if all coins collected
        if (coins.countActive(true) === 0) {
            this.add.text(400, 300, 'YOU WIN!\nPress F5 to restart', {
                fontSize: '48px',
                fill: '#00ff00',
                align: 'center'
            }).setOrigin(0.5);
        }
    }
}