---
layout: default
title: Exploring Accurate and Transparent Domain Adaptation in Predictive Healthcare via Concept-Grounded Orthogonal Inference
---

# Exploring Accurate and Transparent Domain Adaptation in Predictive Healthcare via Concept-Grounded Orthogonal Inference
**arXiv**：[2602.12542v1](https://arxiv.org/abs/2602.12542) · [PDF](https://arxiv.org/pdf/2602.12542.pdf)  
**作者**：Pengfei Hu, Chang Lu, Feifan Liu, Yue Ning  

**一句话要点**：提出ExtraCare通过概念基础正交推理实现准确透明的医疗预测领域适应

**关键词**：领域适应, 电子健康记录预测, 模型可解释性, 正交分解, 概念映射, 临床事件预测

## 3 点简述
- 核心问题：深度学习模型在电子健康记录预测中因数据分布变化导致性能下降，且黑盒特性阻碍临床透明应用。
- 方法要点：将患者表示分解为不变和协变分量，通过监督和正交约束提升预测准确性，并映射稀疏维度到医学概念提供解释。
- 实验或效果：在真实EHR数据集上评估，显示优于特征对齐模型的性能，并通过案例研究验证透明解释能力。

## 摘要（原文）

> Deep learning models for clinical event prediction on electronic health records (EHR) often suffer performance degradation when deployed under different data distributions. While domain adaptation (DA) methods can mitigate such shifts, its "black-box" nature prevents widespread adoption in clinical practice where transparency is essential for trust and safety. We propose ExtraCare to decompose patient representations into invariant and covariant components. By supervising these two components and enforcing their orthogonality during training, our model preserves label information while exposing domain-specific variation at the same time for more accurate predictions than most feature alignment models. More importantly, it offers human-understandable explanations by mapping sparse latent dimensions to medical concepts and quantifying their contributions via targeted ablations. ExtraCare is evaluated on two real-world EHR datasets across multiple domain partition settings, demonstrating superior performance along with enhanced transparency, as evidenced by its accurate predictions and explanations from extensive case studies.

