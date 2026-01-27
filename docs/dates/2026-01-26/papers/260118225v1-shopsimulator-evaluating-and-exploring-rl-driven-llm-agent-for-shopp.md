---
layout: default
title: ShopSimulator: Evaluating and Exploring RL-Driven LLM Agent for Shopping Assistants
---

# ShopSimulator: Evaluating and Exploring RL-Driven LLM Agent for Shopping Assistants
**arXiv**：[2601.18225v1](https://arxiv.org/abs/2601.18225) · [PDF](https://arxiv.org/pdf/2601.18225.pdf)  
**作者**：Pei Wang, Yanan Wu, Xiaoshuai Song, Weixun Wang, Gengru Chen, Zhongwen Li, Kezhong Yan, Ken Deng, Qi Liu, Shuaibing Zhao, Shaopan Xiong, Xuepeng Liu, Xuefeng Chen, Wanxi Deng, Wenbo Su, Bo Zheng  

**一句话要点**：提出ShopSimulator以评估和训练基于强化学习的LLM购物助手代理

**关键词**：购物助手代理, 强化学习, 大语言模型评估, 模拟环境, 个性化搜索

## 3 点简述
- 核心问题：现有研究缺乏统一模拟环境，无法全面评估LLM代理在购物中的个性化搜索和多轮对话能力
- 方法要点：构建大规模中文购物环境ShopSimulator，结合监督微调和强化学习进行训练探索
- 实验或效果：评估显示最佳模型全成功率低于40%，训练后性能显著提升

## 摘要（原文）

> Large language model (LLM)-based agents are increasingly deployed in e-commerce shopping. To perform thorough, user-tailored product searches, agents should interpret personal preferences, engage in multi-turn dialogues, and ultimately retrieve and discriminate among highly similar products. However, existing research has yet to provide a unified simulation environment that consistently captures all of these aspects, and always focuses solely on evaluation benchmarks without training support. In this paper, we introduce ShopSimulator, a large-scale and challenging Chinese shopping environment. Leveraging ShopSimulator, we evaluate LLMs across diverse scenarios, finding that even the best-performing models achieve less than 40% full-success rate. Error analysis reveals that agents struggle with deep search and product selection in long trajectories, fail to balance the use of personalization cues, and to effectively engage with users. Further training exploration provides practical guidance for overcoming these weaknesses, with the combination of supervised fine-tuning (SFT) and reinforcement learning (RL) yielding significant performance improvements. Code and data will be released at https://github.com/ShopAgent-Team/ShopSimulator.

