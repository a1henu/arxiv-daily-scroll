---
layout: default
title: MEME: Modeling the Evolutionary Modes of Financial Markets
---

# MEME: Modeling the Evolutionary Modes of Financial Markets
**arXiv**：[2602.11918v1](https://arxiv.org/abs/2602.11918) · [PDF](https://arxiv.org/pdf/2602.11918.pdf)  
**作者**：Taian Guo, Haiyang Shen, Junyu Luo, Zhongshi Xing, Hanchun Lian, Jinsheng Huang, Binqi Chen, Luchen Liu, Yun Ma, Ming Zhang  

**一句话要点**：提出MEME模型，通过建模投资叙事演化以优化金融市场动态分析与投资组合构建。

**关键词**：金融市场建模, 投资叙事演化, 多智能体提取, 高斯混合模型, 时序对齐, 投资组合优化

## 3 点简述
- 核心问题：现有LLM方法忽视市场驱动逻辑，难以捕捉动态演化共识。
- 方法要点：采用多智能体提取投资论点，高斯混合建模语义共识，并引入时序对齐机制。
- 实验或效果：在2023-2025年中国股票池上超越七种基准，验证了适应市场演化的能力。

## 摘要（原文）

> LLMs have demonstrated significant potential in quantitative finance by processing vast unstructured data to emulate human-like analytical workflows. However, current LLM-based methods primarily follow either an Asset-Centric paradigm focused on individual stock prediction or a Market-Centric approach for portfolio allocation, often remaining agnostic to the underlying reasoning that drives market movements. In this paper, we propose a Logic-Oriented perspective, modeling the financial market as a dynamic, evolutionary ecosystem of competing investment narratives, termed Modes of Thought. To operationalize this view, we introduce MEME (Modeling the Evolutionary Modes of Financial Markets), designed to reconstruct market dynamics through the lens of evolving logics. MEME employs a multi-agent extraction module to transform noisy data into high-fidelity Investment Arguments and utilizes Gaussian Mixture Modeling to uncover latent consensus within a semantic space. To model semantic drift among different market conditions, we also implement a temporal evaluation and alignment mechanism to track the lifecycle and historical profitability of these modes. By prioritizing enduring market wisdom over transient anomalies, MEME ensures that portfolio construction is guided by robust reasoning. Extensive experiments on three heterogeneous Chinese stock pools from 2023 to 2025 demonstrate that MEME consistently outperforms seven SOTA baselines. Further ablation studies, sensitivity analysis, lifecycle case study and cost analysis validate MEME's capacity to identify and adapt to the evolving consensus of financial markets. Our implementation can be found at https://github.com/gta0804/MEME.

