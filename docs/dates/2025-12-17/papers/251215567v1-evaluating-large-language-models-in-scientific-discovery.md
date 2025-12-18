---
layout: default
title: Evaluating Large Language Models in Scientific Discovery
---

# Evaluating Large Language Models in Scientific Discovery
**arXiv**：[2512.15567v1](https://arxiv.org/abs/2512.15567) · [PDF](https://arxiv.org/pdf/2512.15567.pdf)  
**作者**：Zhangde Song, Jieyu Lu, Yuanqi Du, Botao Yu, Thomas M. Pruyn, Yue Huang, Kehan Guo, Xiuzhe Luo, Yuanhao Qu, Yi Qu, Yinkai Wang, Haorui Wang, Jeff Guo, Jingru Gan, Parshin Shojaee, Di Luo, Andres M Bran, Gen Li, Qiyuan Zhao, Shao-Xiong Lennon Luo, Yuxuan Zhang, Xiang Zou, Wanru Zhao, Yifan F. Zhang, Wucheng Zhang, Shunan Zheng, Saiyang Zhang, Sartaaj Takrim Khan, Mahyar Rajabi-Kochi, Samantha Paradi-Maropakis, Tony Baltoiu, Fengyu Xie, Tianyang Chen, Kexin Huang, Weiliang Luo, Meijing Fang, Xin Yang, Lixue Cheng, Jiajun He, Soha Hassoun, Xiangliang Zhang, Wei Wang, Chandan K. Reddy, Chao Zhang, Zhiling Zheng, Mengdi Wang, Le Cong, Carla P. Gomes, Chang-Yu Hsieh, Aditya Nandy, Philippe Schwaller, Heather J. Kulik, Haojun Jia, Huan Sun, Seyed Mohamad Moosavi, Chenru Duan  

**一句话要点**：提出基于场景的基准以评估大语言模型在科学发现中的能力

**关键词**：大语言模型评估, 科学发现基准, 场景化测试, 假设生成, 多学科评估

## 3 点简述
- 核心问题：现有科学基准忽视科学发现所需的迭代推理、假设生成和结果解释。
- 方法要点：引入由领域专家定义的研究项目，分解为模块化场景并采样问题。
- 实验或效果：评估显示模型在科学发现中性能差距大，缩放收益递减，但已展现潜力。

## 摘要（原文）

> Large language models (LLMs) are increasingly applied to scientific research, yet prevailing science benchmarks probe decontextualized knowledge and overlook the iterative reasoning, hypothesis generation, and observation interpretation that drive scientific discovery. We introduce a scenario-grounded benchmark that evaluates LLMs across biology, chemistry, materials, and physics, where domain experts define research projects of genuine interest and decompose them into modular research scenarios from which vetted questions are sampled. The framework assesses models at two levels: (i) question-level accuracy on scenario-tied items and (ii) project-level performance, where models must propose testable hypotheses, design simulations or experiments, and interpret results. Applying this two-phase scientific discovery evaluation (SDE) framework to state-of-the-art LLMs reveals a consistent performance gap relative to general science benchmarks, diminishing return of scaling up model sizes and reasoning, and systematic weaknesses shared across top-tier models from different providers. Large performance variation in research scenarios leads to changing choices of the best performing model on scientific discovery projects evaluated, suggesting all current LLMs are distant to general scientific "superintelligence". Nevertheless, LLMs already demonstrate promise in a great variety of scientific discovery projects, including cases where constituent scenario scores are low, highlighting the role of guided exploration and serendipity in discovery. This SDE framework offers a reproducible benchmark for discovery-relevant evaluation of LLMs and charts practical paths to advance their development toward scientific discovery.

