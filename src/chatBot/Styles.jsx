export const styles = {
    chatWithMeButton: {
        cursor: 'pointer',
        boxShadow: '0px 0px 16px 6px rgba(0, 0, 0, 0.33)',
        backgroundColor: 'white',
        // Border
        borderRadius: '50%',
        // Background 
        backgroundImage: `url('http://localhost:3000/image.png')`, 
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: '44px',
        // Size
        width: '50px',
        height: '50px',
    },
    avatarHello: { 
        // Position
        position: 'absolute', 
        left: 'calc(-100% - 320px - 80px)', 
        top: 'calc(50% - 20px)', 
        // Layering
        zIndex: '10000',
        boxShadow: '0px 0px 16px 6px rgba(0, 0, 0, 0.33)',
        // Border
        padding: '12px 12px 12px 16px',
        borderRadius: '24px', 
        // Color
        backgroundColor: '#EE445E',
        color: 'black',
        //
        fontSize: 'large',
    },
    chatWindow: {
        // Position
        position: 'fixed',
        bottom: '120px',
        right: '30px',
        // Size
        width: '800px',
        height: '750px',
        maxWidth: 'calc(100% - 48px)',
        maxHeight: 'calc(100% - 48px)',
        backgroundColor: 'white',
        // Border
        borderRadius: '12px',
        border: `2px solid #8D0D20`,
        overflow: 'hidden',
        // Shadow
        boxShadow: '0px 0px 16px 6px rgba(0, 0, 0, 0.33)',
    },
}