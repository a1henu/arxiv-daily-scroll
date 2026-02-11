---
layout: default
title: BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation
---

# BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation
**arXiv**：[2602.09383v1](https://arxiv.org/abs/2602.09383) · [PDF](https://arxiv.org/pdf/2602.09383.pdf)  
**作者**：Peng Lai, Zhihao Ou, Yong Wang, Longyue Wang, Jian Yang, Yun Chen, Guanhua Chen  

**一句话要点**：提出BiasScope框架以自动检测LLM-as-a-Judge评估中的潜在偏见

**关键词**：LLM-as-a-Judge, 偏见检测, 自动化框架, 评估鲁棒性, 基准测试

## 3 点简述
- 核心问题：LLM-as-a-Judge评估存在偏见，但未知偏见的自动化探索不足
- 方法要点：BiasScope为LLM驱动框架，可大规模自动发现评估中的潜在偏见
- 实验或效果：在JudgeBench数据集验证有效性，并推出更挑战的JudgeBench-Pro基准

## 摘要（原文）

> LLM-as-a-Judge has been widely adopted across various research and practical applications, yet the robustness and reliability of its evaluation remain a critical issue. A core challenge it faces is bias, which has primarily been studied in terms of known biases and their impact on evaluation outcomes, while automated and systematic exploration of potential unknown biases is still lacking. Nevertheless, such exploration is crucial for enhancing the robustness and reliability of evaluations. To bridge this gap, we propose BiasScope, a LLM-driven framework for automatically and at scale discovering potential biases that may arise during model evaluation. BiasScope can uncover potential biases across different model families and scales, with its generality and effectiveness validated on the JudgeBench dataset. It overcomes the limitations of existing approaches, transforming bias discovery from a passive process relying on manual effort and predefined bias lists into an active and comprehensive automated exploration. Moreover, based on BiasScope, we propose JudgeBench-Pro, an extended version of JudgeBench and a more challenging benchmark for evaluating the robustness of LLM-as-a-judge. Strikingly, even powerful LLMs as evaluators show error rates above 50\% on JudgeBench-Pro, underscoring the urgent need to strengthen evaluation robustness and to mitigate potential biases further.

