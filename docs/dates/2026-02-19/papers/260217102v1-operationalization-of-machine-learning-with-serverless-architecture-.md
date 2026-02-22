---
layout: default
title: Operationalization of Machine Learning with Serverless Architecture: An Industrial Operationalization of Machine Learning with Serverless Architecture: An Industrial Implementation for Harmonized System Code Prediction
---

# Operationalization of Machine Learning with Serverless Architecture: An Industrial Operationalization of Machine Learning with Serverless Architecture: An Industrial Implementation for Harmonized System Code Prediction
**arXiv**：[2602.17102v1](https://arxiv.org/abs/2602.17102) · [PDF](https://arxiv.org/pdf/2602.17102.pdf)  
**作者**：Sai Vineeth Kandappareddigari, Santhoshkumar Jagadish, Gauri Verma, Ilhuicamina Contreras, Christopher Dignam, Anmol Srivastava, Benjamin Demers  

**一句话要点**：提出基于无服务器架构的MLOps框架，用于工业级HS代码预测，实现全生命周期自动化。

**关键词**：无服务器架构, MLOps框架, HS代码预测, 深度学习, 自动化部署, 成本优化

## 3 点简述
- 核心问题：HS代码预测因产品描述短、非结构化且频繁更新而具挑战性，错误可导致贸易延误和损失。
- 方法要点：采用无服务器架构构建模型无关框架，支持事件驱动管道和标准化接口，集成自定义文本嵌入和深度学习模型。
- 实验或效果：Text-CNN模型在真实数据上达到98%准确率，框架确保可重复性、可审计性，并通过自动扩展满足SLA要求。

## 摘要（原文）

> This paper presents a serverless MLOps framework orchestrating the complete ML lifecycle from data ingestion, training, deployment, monitoring, and retraining to using event-driven pipelines and managed services. The architecture is model-agnostic, supporting diverse inference patterns through standardized interfaces, enabling rapid adaptation without infrastructure overhead. We demonstrate practical applicability through an industrial implementation for Harmonized System (HS) code prediction, a compliance-critical task where short, unstructured product descriptions are mapped to standardized codes used by customs authorities in global trade. Frequent updates and ambiguous descriptions make classification challenging, with errors causing shipment delays and financial losses. Our solution uses a custom text embedding encoder and multiple deep learning architectures, with Text-CNN achieving 98 percent accuracy on ground truth data. Beyond accuracy, the pipeline ensures reproducibility, auditability, and SLA adherence under variable loads via auto-scaling. A key feature is automated A/B testing, enabling dynamic model selection and safe promotion in production. Cost-efficiency drives model choice; while transformers may achieve similar accuracy, their long-term operational costs are significantly higher. Deterministic classification with predictable latency and explainability is prioritized, though the architecture remains extensible to transformer variants and LLM-based inference. The paper first introduces the deep learning architectures with simulations and model comparisons, then discusses industrialization through serverless architecture, demonstrating automated retraining, prediction, and validation of HS codes. This work provides a replicable blueprint for operationalizing ML using serverless architecture, enabling enterprises to scale while optimizing performance and economics.

