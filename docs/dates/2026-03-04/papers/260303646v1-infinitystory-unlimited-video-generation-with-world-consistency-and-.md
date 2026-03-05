---
layout: default
title: InfinityStory: Unlimited Video Generation with World Consistency and Character-Aware Shot Transitions
---

# InfinityStory: Unlimited Video Generation with World Consistency and Character-Aware Shot Transitions
**arXiv**：[2603.03646v1](https://arxiv.org/abs/2603.03646) · [PDF](https://arxiv.org/pdf/2603.03646.pdf)  
**作者**：Mohamed Elmoghany, Liangbing Zhao, Xiaoqian Shen, Subhojyoti Mukherjee, Yang Zhou, Gang Wu, Viet Dac Lai, Seunghyun Yoon, Ryan Rossi, Abdullah Rashwan, Puneet Mathur, Varun Manjunatha, Daksh Dangi, Chien Nguyen, Nedim Lipka, Trung Bui, Krishna Kumar Singh, Ruiyi Zhang, Xiaolei Huang, Jaemin Cho, Yu Wang, Namyong Park, Zhengzhong Tu, Hongjie Chen, Hoda Eldardiry, Nesreen Ahmed, Thien Nguyen, Dinesh Manocha, Mohamed Elhoseiny, Franck Dernoncourt  

**一句话要点**：提出InfinityStory框架以生成长篇故事视频，解决背景一致性、多主体镜头过渡和可扩展性问题。

**关键词**：视频生成, 背景一致性, 镜头过渡, 多主体合成, 长视频叙事, 合成数据集

## 3 点简述
- 核心问题：生成长篇故事视频时，背景一致性、多主体镜头过渡和可扩展性存在挑战。
- 方法要点：引入背景一致生成管道和过渡感知视频合成模块，支持多主体动态场景。
- 实验或效果：在VBench上取得最高背景一致性（88.94）和主体一致性（82.11），整体排名最佳（2.80）。

## 摘要（原文）

> Generating long-form storytelling videos with consistent visual narratives remains a significant challenge in video synthesis. We present a novel framework, dataset, and a model that address three critical limitations: background consistency across shots, seamless multi-subject shot-to-shot transitions, and scalability to hour-long narratives. Our approach introduces a background-consistent generation pipeline that maintains visual coherence across scenes while preserving character identity and spatial relationships. We further propose a transition-aware video synthesis module that generates smooth shot transitions for complex scenarios involving multiple subjects entering or exiting frames, going beyond the single-subject limitations of prior work. To support this, we contribute with a synthetic dataset of 10,000 multi-subject transition sequences covering underrepresented dynamic scene compositions. On VBench, InfinityStory achieves the highest Background Consistency (88.94), highest Subject Consistency (82.11), and the best overall average rank (2.80), showing improved stability, smoother transitions, and better temporal coherence.

