---
layout: default
title: Optimising antibiotic switching via forecasting of patient physiology
---

# Optimising antibiotic switching via forecasting of patient physiology
**arXiv**：[2603.08242v1](https://arxiv.org/abs/2603.08242) · [PDF](https://arxiv.org/pdf/2603.08242.pdf)  
**作者**：Magnus Ross, Nel Swanepoel, Akish Luintel, Emma McGuire, Ingemar J. Cox, Steve Harris, Vasileios Lampos  

**一句话要点**：提出基于神经过程的患者生理轨迹预测方法，以优化抗生素静脉转口服的临床决策支持。

**关键词**：抗生素管理, 临床决策支持, 神经过程, 生理轨迹预测, 患者优先级排序

## 3 点简述
- 核心问题：临床实践中抗生素静脉转口服延迟或不一致，影响患者住院时间和医疗成本。
- 方法要点：使用神经过程概率建模生命体征轨迹，通过预测与指南比较评估转换准备度，而非学习历史决策。
- 实验或效果：在MIMIC-IV和UCLH数据集验证，系统选择相关患者数量比随机方法高2.2-3.2倍。

## 摘要（原文）

> Timely transition from intravenous (IV) to oral antibiotic therapy shortens hospital stays, reduces catheter-related infections, and lowers healthcare costs, yet one in five patients in England remain on IV antibiotics despite meeting switching criteria. Clinical decision support systems can improve switching rates, but approaches that learn from historical decisions reproduce the delays and inconsistencies of routine practice. We propose using neural processes to model vital sign trajectories probabilistically, predicting switch-readiness by comparing forecasts against clinical guidelines rather than learning from past actions, and ranking patients to prioritise clinical review. The design yields interpretable outputs, adapts to updated guidelines without retraining, and preserves clinical judgement. Validated on MIMIC-IV (US intensive care, 6,333 encounters) and UCLH (a large urban academic UK hospital group, 10,584 encounters), the system selects 2.2-3.2$\times$ more relevant patients than random. Our results demonstrate that forecasting patient physiology offers a principled foundation for decision support in antibiotic stewardship.

