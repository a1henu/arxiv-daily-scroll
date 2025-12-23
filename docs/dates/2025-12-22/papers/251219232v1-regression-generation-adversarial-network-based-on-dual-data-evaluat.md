---
layout: default
title: Regression generation adversarial network based on dual data evaluation strategy for industrial application
---

# Regression generation adversarial network based on dual data evaluation strategy for industrial application
**arXiv**：[2512.19232v1](https://arxiv.org/abs/2512.19232) · [PDF](https://arxiv.org/pdf/2512.19232.pdf)  
**作者**：Zesen Wang, Yonggang Li, Lijuan Lan  

**一句话要点**：提出基于双数据评估策略的回归生成对抗网络，以解决工业软测量中数据不足问题。

**关键词**：软测量, 生成对抗网络, 回归生成, 多任务学习, 数据增强, 工业应用

## 3 点简述
- 核心问题：工业软测量中数据不足，传统GAN忽略标签与特征映射关系，影响性能与效率。
- 方法要点：集成回归信息到判别器和生成器，采用浅层共享机制，设计双数据评估策略提升样本多样性和泛化能力。
- 实验或效果：在废水处理、地表水、CO₂吸收塔和工业燃气轮机四个案例中验证方法优越性。

## 摘要（原文）

> Soft sensing infers hard-to-measure data through a large number of easily obtainable variables. However, in complex industrial scenarios, the issue of insufficient data volume persists, which diminishes the reliability of soft sensing. Generative Adversarial Networks (GAN) are one of the effective solutions for addressing insufficient samples. Nevertheless, traditional GAN fail to account for the mapping relationship between labels and features, which limits further performance improvement. Although some studies have proposed solutions, none have considered both performance and efficiency simultaneously. To address these problems, this paper proposes the multi-task learning-based regression GAN framework that integrates regression information into both the discriminator and generator, and implements a shallow sharing mechanism between the discriminator and regressor. This approach significantly enhances the quality of generated samples while improving the algorithm's operational efficiency. Moreover, considering the importance of training samples and generated samples, a dual data evaluation strategy is designed to make GAN generate more diverse samples, thereby increasing the generalization of subsequent modeling. The superiority of method is validated through four classic industrial soft sensing cases: wastewater treatment plants, surface water, $CO_2$ absorption towers, and industrial gas turbines.

