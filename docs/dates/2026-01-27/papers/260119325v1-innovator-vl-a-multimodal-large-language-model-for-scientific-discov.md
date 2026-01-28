---
layout: default
title: Innovator-VL: A Multimodal Large Language Model for Scientific Discovery
---

# Innovator-VL: A Multimodal Large Language Model for Scientific Discovery
**arXiv**：[2601.19325v1](https://arxiv.org/abs/2601.19325) · [PDF](https://arxiv.org/pdf/2601.19325.pdf)  
**作者**：Zichen Wen, Boxue Yang, Shuang Chen, Yaojie Zhang, Yuhang Han, Junlong Ke, Cong Wang, Yicheng Fu, Jiawang Zhao, Jiangchao Yao, Xi Fang, Zhen Wang, Henxing Cai, Lin Yao, Zhifeng Gao, Yanhui Hong, Nang Yuan, Yixuan Li, Guojiang Zhao, Haoyi Tao, Nan Wang, Han Lyu, Guolin Ke, Ning Liao, Xiaoxing Wang, Kai Chen, Zhiyu Li, Feiyu Xiong, Sihan Hu, Kun Chen, Yanfeng Wang, Weinan E, Linfeng Zhang, Linfeng Zhang  

**一句话要点**：提出Innovator-VL，通过透明训练与高效数据实现科学多模态理解与推理。

**关键词**：科学多模态大语言模型, 透明训练管道, 数据效率, 多模态推理, 科学发现

## 3 点简述
- 核心问题：科学多模态模型依赖大规模数据与不透明流程，导致效率低、可复现性差。
- 方法要点：采用端到端透明训练管道，包括数据清洗、监督微调、强化学习，强调数据选择而非盲目扩展。
- 实验或效果：使用少于五百万样本，在科学任务和通用视觉基准上实现竞争性能，展示强泛化能力。

## 摘要（原文）

> We present Innovator-VL, a scientific multimodal large language model designed to advance understanding and reasoning across diverse scientific domains while maintaining excellent performance on general vision tasks. Contrary to the trend of relying on massive domain-specific pretraining and opaque pipelines, our work demonstrates that principled training design and transparent methodology can yield strong scientific intelligence with substantially reduced data requirements. (i) First, we provide a fully transparent, end-to-end reproducible training pipeline, covering data collection, cleaning, preprocessing, supervised fine-tuning, reinforcement learning, and evaluation, along with detailed optimization recipes. This facilitates systematic extension by the community. (ii) Second, Innovator-VL exhibits remarkable data efficiency, achieving competitive performance on various scientific tasks using fewer than five million curated samples without large-scale pretraining. These results highlight that effective reasoning can be achieved through principled data selection rather than indiscriminate scaling. (iii) Third, Innovator-VL demonstrates strong generalization, achieving competitive performance on general vision, multimodal reasoning, and scientific benchmarks. This indicates that scientific alignment can be integrated into a unified model without compromising general-purpose capabilities. Our practices suggest that efficient, reproducible, and high-performing scientific multimodal models can be built even without large-scale data, providing a practical foundation for future research.

