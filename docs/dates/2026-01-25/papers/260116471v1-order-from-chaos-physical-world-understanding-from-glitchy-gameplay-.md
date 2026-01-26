---
layout: default
title: Order from Chaos: Physical World Understanding from Glitchy Gameplay Videos
---

# Order from Chaos: Physical World Understanding from Glitchy Gameplay Videos
**arXiv**：[2601.16471v1](https://arxiv.org/abs/2601.16471) · [PDF](https://arxiv.org/pdf/2601.16471.pdf)  
**作者**：Meng Cao, Haoran Tang, Haoze Zhao, Mingfei Han, Ruyang Liu, Qiang Sun, Xiaojun Chang, Ian Reid, Xiaodan Liang  

**一句话要点**：提出利用游戏视频故障作为监督源，构建PhysGame数据集以增强物理世界理解

**关键词**：物理世界理解, 游戏视频分析, 多模态大语言模型, 异常检测, 指令调优数据集

## 3 点简述
- 核心问题：现有物理理解数据集成本高或真实性不足，多模态大模型物理推理能力有限。
- 方法要点：利用游戏视频中的物理异常作为监督，构建包含14万问答对的PhysGame数据集，并设计元信息引导的提示策略。
- 实验或效果：PhysGame提升模型在真实世界和通用基准上的性能，GameBench评估显示检测物理不合理性的鲁棒性增强。

## 摘要（原文）

> Understanding the physical world, including object dynamics, material properties, and causal interactions, remains a core challenge in artificial intelligence. Although recent multi-modal large language models (MLLMs) have demonstrated impressive general reasoning capabilities, they still fall short of achieving human-level understanding of physical principles. Existing datasets for physical reasoning either rely on real-world videos, which incur high annotation costs, or on synthetic simulations, which suffer from limited realism and diversity. In this paper, we propose a novel paradigm that leverages glitches in gameplay videos, referring to visual anomalies that violate predefined physical laws, as a rich and scalable supervision source for physical world understanding. We introduce PhysGame, an meta information guided instruction-tuning dataset containing 140,057 glitch-centric question-answer pairs across five physical domains and sixteen fine-grained categories. To ensure data accuracy, we design a prompting strategy that utilizes gameplay metadata such as titles and descriptions to guide high-quality QA generation. Complementing PhysGame, we construct GameBench, an expert-annotated benchmark with 880 glitch-identified gameplay videos designed to evaluate physical reasoning capabilities. Extensive experiments show that PhysGame significantly enhances both Game2Real transferability, improving the real world physical reasoning performance of Qwen2.5VL by 2.5% on PhysBench, and Game2General transferability, yielding a 1.9% gain on the MVBench benchmark. Moreover, PhysGame-tuned models achieve a 3.7% absolute improvement on GameBench, demonstrating enhanced robustness in detecting physical implausibilities. These results indicate that learning from gameplay anomalies offers a scalable and effective pathway toward advancing physical world understanding in multimodal intelligence.

