---
layout: default
title: Wow, wo, val! A Comprehensive Embodied World Model Evaluation Turing Test
---

# Wow, wo, val! A Comprehensive Embodied World Model Evaluation Turing Test
**arXiv**：[2601.04137v1](https://arxiv.org/abs/2601.04137) · [PDF](https://arxiv.org/pdf/2601.04137.pdf)  
**作者**：Chun-Kai Fan, Xiaowei Chi, Xiaozhu Ju, Hao Li, Yong Bao, Yu-Kai Wang, Lizhang Chen, Zhiyuan Jiang, Kuangzhi Ge, Ying Li, Weishi Mi, Qingpo Wuwu, Peidong Jia, Yulin Luo, Kevin Zhang, Zhiyuan Qin, Yong Dai, Sirui Han, Yike Guo, Shanghang Zhang, Jian Tang  

**一句话要点**：提出WoW-World-Eval基准以评估具身AI中世界模型的感知保真度与鲁棒性

**关键词**：具身AI, 世界模型评估, 视频基础模型, 机器人操作, 感知保真度, 逆动态模型

## 3 点简述
- 核心问题：视频基础模型在具身AI中是否具备足够的生成泛化能力和鲁棒性作为通用先验
- 方法要点：基于609个机器人操作数据构建基准，评估感知、规划、预测、泛化和执行五项核心能力
- 实验或效果：模型在长时规划得分17.27，物理一致性最高68.02，WoW模型在逆动态模型测试中成功率40.74%

## 摘要（原文）

> As world models gain momentum in Embodied AI, an increasing number of works explore using video foundation models as predictive world models for downstream embodied tasks like 3D prediction or interactive generation. However, before exploring these downstream tasks, video foundation models still have two critical questions unanswered: (1) whether their generative generalization is sufficient to maintain perceptual fidelity in the eyes of human observers, and (2) whether they are robust enough to serve as a universal prior for real-world embodied agents. To provide a standardized framework for answering these questions, we introduce the Embodied Turing Test benchmark: WoW-World-Eval (Wow,wo,val). Building upon 609 robot manipulation data, Wow-wo-val examines five core abilities, including perception, planning, prediction, generalization, and execution. We propose a comprehensive evaluation protocol with 22 metrics to assess the models' generation ability, which achieves a high Pearson Correlation between the overall score and human preference (>0.93) and establishes a reliable foundation for the Human Turing Test. On Wow-wo-val, models achieve only 17.27 on long-horizon planning and at best 68.02 on physical consistency, indicating limited spatiotemporal consistency and physical reasoning. For the Inverse Dynamic Model Turing Test, we first use an IDM to evaluate the video foundation models' execution accuracy in the real world. However, most models collapse to $\approx$ 0% success, while WoW maintains a 40.74% success rate. These findings point to a noticeable gap between the generated videos and the real world, highlighting the urgency and necessity of benchmarking World Model in Embodied AI.

