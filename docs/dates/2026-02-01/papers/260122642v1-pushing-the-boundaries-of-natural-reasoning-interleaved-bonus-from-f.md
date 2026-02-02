---
layout: default
title: Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification
---

# Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification
**arXiv**：[2601.22642v1](https://arxiv.org/abs/2601.22642) · [PDF](https://arxiv.org/pdf/2601.22642.pdf)  
**作者**：Chuxue Cao, Jinluan Yang, Haoran Li, Kunhao Pan, Zijian Zhao, Zhengyu Chen, Yuchen Tian, Lijun Wu, Conghui He, Sirui Han, Yike Guo  

**一句话要点**：提出形式逻辑验证引导框架，通过动态交织验证与生成过程提升大语言模型推理性能。

**关键词**：形式逻辑验证, 神经符号方法, 推理性能提升, 大语言模型, 动态交织框架

## 3 点简述
- 核心问题：大语言模型因随机性导致逻辑不一致和奖励攻击，形式符号系统可避免此问题。
- 方法要点：引入形式逻辑验证引导框架，实时检测并纠正推理链中的错误，区别于被动后验方法。
- 实验或效果：在六个基准测试中，7B和14B模型平均超越基线10.4%和14.2%，验证了可扩展性。

## 摘要（原文）

> Large Language Models (LLMs) show remarkable capabilities, yet their stochastic next-token prediction creates logical inconsistencies and reward hacking that formal symbolic systems avoid. To bridge this gap, we introduce a formal logic verification-guided framework that dynamically interleaves formal symbolic verification with the natural language generation process, providing real-time feedback to detect and rectify errors as they occur. Distinguished from previous neuro-symbolic methods limited by passive post-hoc validation, our approach actively penalizes intermediate fallacies during the reasoning chain. We operationalize this framework via a novel two-stage training pipeline that synergizes formal logic verification-guided supervised fine-tuning and policy optimization. Extensive evaluation on six benchmarks spanning mathematical, logical, and general reasoning demonstrates that our 7B and 14B models outperform state-of-the-art baselines by average margins of 10.4% and 14.2%, respectively. These results validate that formal verification can serve as a scalable mechanism to significantly push the performance boundaries of advanced LLM reasoning.

