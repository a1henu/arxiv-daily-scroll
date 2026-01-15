---
layout: default
title: Mi:dm 2.0 Korea-centric Bilingual Language Models
---

# Mi:dm 2.0 Korea-centric Bilingual Language Models
**arXiv**：[2601.09066v1](https://arxiv.org/abs/2601.09066) · [PDF](https://arxiv.org/pdf/2601.09066.pdf)  
**作者**：Donghoon Shin, Sejung Lee, Soonmin Bae, Hwijung Ryu, Changwon Ok, Hoyoun Jung, Hyesung Ji, Jeehyun Lim, Jehoon Lee, Ji-Eun Han, Jisoo Baik, Mihyeon Kim, Riwoo Chung, Seongmin Lee, Wonjae Park, Yoonseok Heo, Youngkyung Seo, Seyoun Won, Boeun Kim, Cheolhun Heo, Eunkyeong Lee, Honghee Lee, Hyeongju Ju, Hyeontae Seo, Jeongyong Shim, Jisoo Lee, Junseok Koh, Junwoo Kim, Minho Lee, Minji Kang, Minju Kim, Sangha Nam, Seongheum Park, Taehyeong Kim, Euijai Ahn, Hong Seok Jeung, Jisu Shin, Jiyeon Kim, Seonyeong Song, Seung Hyun Kong, Sukjin Hong, Taeyang Yun, Yu-Seon Kim, A-Hyun Lee, Chae-Jeong Lee, Hye-Won Yu, Ji-Hyun Ahn, Song-Yeon Kim, Sun-Woo Jung, Eunju Kim, Eunji Ha, Jinwoo Baek, Yun-ji Lee, Wanjin Park, Jeong Yeop Kim, Eun Mi Kim, Hyoung Jun Park, Jung Won Yoon, Min Sung Noh, Myung Gyo Oh, Wongyoung Lee, Yun Jin Park, Young S. Kwon, Hyun Keun Kim, Jieun Lee, YeoJoo Park  

**一句话要点**：提出Mi:dm 2.0双语大语言模型以解决韩国中心AI中的文化对齐与数据质量不足问题。

**关键词**：双语大语言模型, 韩国中心AI, 文化对齐, 数据质量优化, 课程学习, 韩语分词器

## 3 点简述
- 核心问题：现有LLM因韩语数据不足、质量低且缺乏文化对齐，导致韩国语境理解受限。
- 方法要点：通过专有数据清洗、高质量合成数据生成、课程学习策略混合数据及定制韩语优化分词器提升模型性能。
- 实验或效果：在KMMLU等韩国基准测试中实现零样本SOTA，并在语言、人文社科任务中表现优异。

## 摘要（原文）

> We introduce Mi:dm 2.0, a bilingual large language model (LLM) specifically engineered to advance Korea-centric AI. This model goes beyond Korean text processing by integrating the values, reasoning patterns, and commonsense knowledge inherent to Korean society, enabling nuanced understanding of cultural contexts, emotional subtleties, and real-world scenarios to generate reliable and culturally appropriate responses. To address limitations of existing LLMs, often caused by insufficient or low-quality Korean data and lack of cultural alignment, Mi:dm 2.0 emphasizes robust data quality through a comprehensive pipeline that includes proprietary data cleansing, high-quality synthetic data generation, strategic data mixing with curriculum learning, and a custom Korean-optimized tokenizer to improve efficiency and coverage. To realize this vision, we offer two complementary configurations: Mi:dm 2.0 Base (11.5B parameters), built with a depth-up scaling strategy for general-purpose use, and Mi:dm 2.0 Mini (2.3B parameters), optimized for resource-constrained environments and specialized tasks. Mi:dm 2.0 achieves state-of-the-art performance on Korean-specific benchmarks, with top-tier zero-shot results on KMMLU and strong internal evaluation results across language, humanities, and social science tasks. The Mi:dm 2.0 lineup is released under the MIT license to support extensive research and commercial use. By offering accessible and high-performance Korea-centric LLMs, KT aims to accelerate AI adoption across Korean industries, public services, and education, strengthen the Korean AI developer community, and lay the groundwork for the broader vision of K-intelligence. Our models are available at https://huggingface.co/K-intelligence. For technical inquiries, please contact midm-llm@kt.com.

