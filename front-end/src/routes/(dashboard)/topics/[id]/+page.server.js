export async function load({ params }) {
    const topics = [
        {
            id: 1,
            img: '/images/topic com.jpg',
            title: 'Giao tiếp cơ bản',
            description: 'Description for Giao tiếp cơ bản',
            vocabulary: ['word1', 'word2']
        },
        {
            id: 2,
            img: '/images/topic family.jpg',
            title: 'Gia đình',
            description: 'Description for Gia đình',
            vocabulary: ['word1', 'word2']
        },
        {
            id: 3,
            img: '/images/topic school.jpg',
            title: 'Trường học',
            description: 'Description for Trường học',
            vocabulary: ['word1', 'word2']
        },
        {
            id: 4,
            img: '/images/topic weather.jpg',
            title: 'Thời tiết',
            description: 'Description for Thời tiết',
            vocabulary: ['word1', 'word2']
        }
    ];

    const topic = topics.find((t) => t.id === Number(params.id));

    if (!topic) {
        return {
            status: 404,
            error: new Error('Topic not found')
        };
    }

    return { 
        topic 
    };
}