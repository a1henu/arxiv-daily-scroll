---
layout: default
title: Ostrakon-VL: Towards Domain-Expert MLLM for Food-Service and Retail Stores
---

# Ostrakon-VL: Towards Domain-Expert MLLM for Food-Service and Retail Stores
**arXiv**：[2601.21342v1](https://arxiv.org/abs/2601.21342) · [PDF](https://arxiv.org/pdf/2601.21342.pdf)  
**作者**：Zhiyong Shen, Gongpeng Zhao, Jun Zhou, Li Yu, Guandong Kou, Jichen Li, Chuanlei Dong, Zuncheng Li, Kaimao Li, Bingkun Wei, Shicheng Hu, Wei Xia, Wenguo Duan  

**一句话要点**：提出Ostrakon-VL模型、ShopBench基准和QUAD数据管道，以解决食品服务和零售场景中MLLM部署的挑战。

**关键词**：多模态大语言模型, 食品服务零售场景, 基准测试, 数据管道, 参数效率

## 3 点简述
- 核心问题：食品服务和零售场景数据噪声大且缺乏标准化评估，阻碍MLLM部署。
- 方法要点：基于Qwen3-VL-8B开发Ostrakon-VL，引入ShopBench基准和QUAD数据管道。
- 实验或效果：Ostrakon-VL在ShopBench上平均得分60.1，超越更大规模模型，提升参数效率。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have recently achieved substantial progress in general-purpose perception and reasoning. Nevertheless, their deployment in Food-Service and Retail Stores (FSRS) scenarios encounters two major obstacles: (i) real-world FSRS data, collected from heterogeneous acquisition devices, are highly noisy and lack auditable, closed-loop data curation, which impedes the construction of high-quality, controllable, and reproducible training corpora; and (ii) existing evaluation protocols do not offer a unified, fine-grained and standardized benchmark spanning single-image, multi-image, and video inputs, making it challenging to objectively gauge model robustness. To address these challenges, we first develop Ostrakon-VL, an FSRS-oriented MLLM based on Qwen3-VL-8B. Second, we introduce ShopBench, the first public benchmark for FSRS. Third, we propose QUAD (Quality-aware Unbiased Automated Data-curation), a multi-stage multimodal instruction data curation pipeline. Leveraging a multi-stage training strategy, Ostrakon-VL achieves an average score of 60.1 on ShopBench, establishing a new state of the art among open-source MLLMs with comparable parameter scales and diverse architectures. Notably, it surpasses the substantially larger Qwen3-VL-235B-A22B (59.4) by +0.7, and exceeds the same-scale Qwen3-VL-8B (55.3) by +4.8, demonstrating significantly improved parameter efficiency. These results indicate that Ostrakon-VL delivers more robust and reliable FSRS-centric perception and decision-making capabilities. To facilitate reproducible research, we will publicly release Ostrakon-VL and the ShopBench benchmark.

