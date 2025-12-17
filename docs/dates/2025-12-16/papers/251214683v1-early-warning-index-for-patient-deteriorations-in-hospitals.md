---
layout: default
title: Early Warning Index for Patient Deteriorations in Hospitals
---

# Early Warning Index for Patient Deteriorations in Hospitals
**arXiv**：[2512.14683v1](https://arxiv.org/abs/2512.14683) · [PDF](https://arxiv.org/pdf/2512.14683.pdf)  
**作者**：Dimitris Bertsimas, Yu Ma, Kimberly Villalobos Carballo, Gagan Singh, Michal Laskowski, Jeff Mather, Dan Kombert, Howard Haronian  

**一句话要点**：提出早期预警指数（EWI）以解决医院患者恶化风险预测问题

**关键词**：患者恶化预测, 多模态机器学习, 可解释人工智能, 电子健康记录, 临床决策支持, 风险分层

## 3 点简述
- 核心问题：医院缺乏自动化系统整合异构临床数据预测关键事件，数据格式不一致阻碍准确风险评估。
- 方法要点：开发多模态机器学习框架EWI，结合人机交互过程，使用SHAP解释模型输出，从结构化与非结构化EHR数据自动提取特征。
- 实验或效果：在18,633名患者数据集上实现C统计量0.796，部署为风险分层仪表板，节省医生时间并优化资源分配。

## 摘要（原文）

> Hospitals lack automated systems to harness the growing volume of heterogeneous clinical and operational data to effectively forecast critical events. Early identification of patients at risk for deterioration is essential not only for patient care quality monitoring but also for physician care management. However, translating varied data streams into accurate and interpretable risk assessments poses significant challenges due to inconsistent data formats. We develop a multimodal machine learning framework, the Early Warning Index (EWI), to predict the aggregate risk of ICU admission, emergency response team dispatch, and mortality. Key to EWI's design is a human-in-the-loop process: clinicians help determine alert thresholds and interpret model outputs, which are enhanced by explainable outputs using Shapley Additive exPlanations (SHAP) to highlight clinical and operational factors (e.g., scheduled surgeries, ward census) driving each patient's risk. We deploy EWI in a hospital dashboard that stratifies patients into three risk tiers. Using a dataset of 18,633 unique patients at a large U.S. hospital, our approach automatically extracts features from both structured and unstructured electronic health record (EHR) data and achieves C-statistics of 0.796. It is currently used as a triage tool for proactively managing at-risk patients. The proposed approach saves physicians valuable time by automatically sorting patients of varying risk levels, allowing them to concentrate on patient care rather than sifting through complex EHR data. By further pinpointing specific risk drivers, the proposed model provides data-informed adjustments to caregiver scheduling and allocation of critical resources. As a result, clinicians and administrators can avert downstream complications, including costly procedures or high readmission rates and improve overall patient flow.

