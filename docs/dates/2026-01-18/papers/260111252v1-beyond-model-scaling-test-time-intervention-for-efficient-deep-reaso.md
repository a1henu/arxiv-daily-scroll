---
layout: default
title: Beyond Model Scaling: Test-Time Intervention for Efficient Deep Reasoning
---

# Beyond Model Scaling: Test-Time Intervention for Efficient Deep Reasoning
**arXiv**：[2601.11252v1](https://arxiv.org/abs/2601.11252) · [PDF](https://arxiv.org/pdf/2601.11252.pdf)  
**作者**：Qianyue Wang, Jinwu Hu, Yufeng Wang, Huanxiang Lin, Bolin Chen, Zhiquan Wen, Yaofo Chen, Mingkui Tan  

**一句话要点**：提出Think-with-Me测试时交互推理范式，通过外部反馈干预解决大型推理模型效率低下问题。

**关键词**：测试时干预, 交互推理, 大型推理模型, 效率优化, 多步推理, 外部反馈

## 3 点简述
- 核心问题：大型推理模型存在过度思考和偏离等低效推理，增加计算成本并降低性能。
- 方法要点：在推理过程中暂停于过渡连词点，引入基于多标准评估的外部反馈，自适应调整推理长度。
- 实验或效果：在AIME24上，相比QwQ-32B，准确率提升7.19%，平均推理长度减少81%。

## 摘要（原文）

> Large Reasoning Models (LRMs) excel at multi-step reasoning but often suffer from inefficient reasoning processes like overthinking and overshoot, where excessive or misdirected reasoning increases computational cost and degrades performance. Existing efficient reasoning methods operate in a closed-loop manner, lacking mechanisms for external intervention to guide the reasoning process. To address this, we propose Think-with-Me, a novel test-time interactive reasoning paradigm that introduces external feedback intervention into the reasoning process. Our key insights are that transitional conjunctions serve as natural points for intervention, signaling phases of self-validation or exploration and using transitional words appropriately to prolong the reasoning enhances performance, while excessive use affects performance. Building on these insights, Think-with-Me pauses reasoning at these points for external feedback, adaptively extending or terminating reasoning to reduce redundancy while preserving accuracy. The feedback is generated via a multi-criteria evaluation (rationality and completeness) and comes from either human or LLM proxies. We train the target model using Group Relative Policy Optimization (GRPO) to adapt to this interactive mode. Experiments show that Think-with-Me achieves a superior balance between accuracy and reasoning length under limited context windows. On AIME24, Think-with-Me outperforms QwQ-32B by 7.19% in accuracy while reducing average reasoning length by 81% under an 8K window. The paradigm also benefits security and creative tasks.

