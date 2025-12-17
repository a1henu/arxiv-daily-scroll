---
layout: default
title: OpenDataArena: A Fair and Open Arena for Benchmarking Post-Training Dataset Value
---

# OpenDataArena: A Fair and Open Arena for Benchmarking Post-Training Dataset Value
**arXiv**：[2512.14051v1](https://arxiv.org/abs/2512.14051) · [PDF](https://arxiv.org/pdf/2512.14051.pdf)  
**作者**：Mengzhang Cai, Xin Gao, Yu Li, Honglin Lin, Zheng Liu, Zhuoshi Pan, Qizhi Pei, Xiaoran Shang, Mengyuan Sun, Zinan Tang, Xiaoyang Wang, Zhanping Zhong, Yun Zhu, Dahua Lin, Conghui He, Lijun Wu  

**一句话要点**：提出OpenDataArena以公平开放地评估后训练数据集价值

**关键词**：后训练数据集评估, 数据质量评分, 数据谱系分析, 开源基准平台, 数据为中心AI

## 3 点简述
- 核心问题：后训练数据集质量与多样性评估不透明，阻碍模型可复现性与数据-行为因果分析。
- 方法要点：构建统一训练-评估流程、多维评分框架、数据谱系探索器和开源工具包。
- 实验或效果：覆盖120+数据集、22个基准，揭示数据复杂度与性能权衡，识别冗余并映射谱系关系。

## 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) is predicated on the quality and diversity of post-training datasets. However, a critical dichotomy persists: while models are rigorously benchmarked, the data fueling them remains a black box--characterized by opaque composition, uncertain provenance, and a lack of systematic evaluation. This opacity hinders reproducibility and obscures the causal link between data characteristics and model behaviors. To bridge this gap, we introduce OpenDataArena (ODA), a holistic and open platform designed to benchmark the intrinsic value of post-training data. ODA establishes a comprehensive ecosystem comprising four key pillars: (i) a unified training-evaluation pipeline that ensures fair, open comparisons across diverse models (e.g., Llama, Qwen) and domains; (ii) a multi-dimensional scoring framework that profiles data quality along tens of distinct axes; (iii) an interactive data lineage explorer to visualize dataset genealogy and dissect component sources; and (iv) a fully open-source toolkit for training, evaluation, and scoring to foster data research. Extensive experiments on ODA--covering over 120 training datasets across multiple domains on 22 benchmarks, validated by more than 600 training runs and 40 million processed data points--reveal non-trivial insights. Our analysis uncovers the inherent trade-offs between data complexity and task performance, identifies redundancy in popular benchmarks through lineage tracing, and maps the genealogical relationships across datasets. We release all results, tools, and configurations to democratize access to high-quality data evaluation. Rather than merely expanding a leaderboard, ODA envisions a shift from trial-and-error data curation to a principled science of Data-Centric AI, paving the way for rigorous studies on data mixing laws and the strategic composition of foundation models.

