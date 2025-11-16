---
layout: default
title: Learning to Pose Problems: Reasoning-Driven and Solver-Adaptive Data Synthesis for Large Reasoning Models
---

# Learning to Pose Problems: Reasoning-Driven and Solver-Adaptive Data Synthesis for Large Reasoning Models
**arXiv**：[2511.09907v1](https://arxiv.org/abs/2511.09907) · [PDF](https://arxiv.org/pdf/2511.09907.pdf)  
**作者**：Yongxian Wei, Yilin Zhao, Li Shen, Xinrui Chen, Runxi Cheng, Sinan Du, Hao Yu, Gang Liu, Jiahong Yan, Chun Yuan, Dian Li  

**一句话要点**：提出推理驱动和求解器自适应的数据合成方法，以提升大型推理模型的训练效果。

**关键词**：数据合成, 推理模型, 问题生成, 自适应难度, 模型训练, 性能提升

## 3 点简述
- 现有数据合成方法忽视求解器能力，生成低价值问题或依赖复杂流程平衡难度。
- 方法通过推理模型规划问题方向，并基于求解器反馈自适应调整问题难度。
- 在10个基准测试中平均提升2.5%，并支持语言和视觉语言模型的泛化。

## 摘要（原文）

> Data synthesis for training large reasoning models offers a scalable alternative to limited, human-curated datasets, enabling the creation of high-quality data. However, existing approaches face several challenges: (i) indiscriminate generation that ignores the solver's ability and yields low-value problems, or reliance on complex data pipelines to balance problem difficulty; and (ii) a lack of reasoning in problem generation, leading to shallow problem variants. In this paper, we develop a problem generator that reasons explicitly to plan problem directions before synthesis and adapts difficulty to the solver's ability. Specifically, we construct related problem pairs and augment them with intermediate problem-design CoT produced by a reasoning model. These data bootstrap problem-design strategies from the generator. Then, we treat the solver's feedback on synthetic problems as a reward signal, enabling the generator to calibrate difficulty and produce complementary problems near the edge of the solver's competence. Extensive experiments on 10 mathematical and general reasoning benchmarks show that our method achieves an average improvement of 2.5% and generalizes to both language and vision-language models. Moreover, a solver trained on the synthesized data provides improved rewards for continued generator training, enabling co-evolution and yielding a further 0.7% performance gain. Our code will be made publicly available here.

