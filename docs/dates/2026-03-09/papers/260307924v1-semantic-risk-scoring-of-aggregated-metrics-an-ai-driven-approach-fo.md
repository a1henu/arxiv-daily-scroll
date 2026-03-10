---
layout: default
title: Semantic Risk Scoring of Aggregated Metrics: An AI-Driven Approach for Healthcare Data Governance
---

# Semantic Risk Scoring of Aggregated Metrics: An AI-Driven Approach for Healthcare Data Governance
**arXiv**：[2603.07924v1](https://arxiv.org/abs/2603.07924) · [PDF](https://arxiv.org/pdf/2603.07924.pdf)  
**作者**：Mohammed Omer Shakeel Ahmed  

**一句话要点**：提出基于AI的语义风险评分框架，以解决医疗聚合指标隐私泄露问题

**关键词**：医疗数据治理, 隐私风险评估, SQL查询分析, AI驱动框架, 聚合指标安全

## 3 点简述
- 核心问题：医疗聚合指标在跨部门共享时可能无意中泄露隐私，需静态检测风险
- 方法要点：解析SQL查询为AST，提取敏感模式，融合CodeBERT嵌入与结构特征，用XGBoost分类器评分
- 实验或效果：系统能主动标记高风险查询，支持预执行保护，提升合规性和可审计性

## 摘要（原文）

> Large healthcare institutions typically operate multiple business intelligence (BI) teams segmented by domain, including clinical performance, fundraising, operations, and compliance. Due to HIPAA, FERPA, and IRB restrictions, these teams face challenges in sharing patient-level data needed for analytics. To mitigate this, A metric aggregation table is proposed, which is a precomputed, privacy-compliant summary. These abstractions enable decision-making without direct access to sensitive data. However, even aggregated metrics can inadvertently lead to privacy risks if constructed without rigorous safeguards. A modular AI framework is proposed that evaluates SQL-based metric definitions for potential overexposure using both semantic and syntactic features. Specifically, the system parses SQL queries into abstract syntax trees (ASTs), extracts sensitive patterns (e.g., fine-grained GROUP BY on ZIP code or gender), and encodes the logic using pretrained CodeBERT embeddings. These are fused with structural features and passed to an XGBoost classifier trained to assign risk scores. Queries that surpass the risk threshold (e.g., > 0.85) are flagged and returned with human-readable explanations. This enables proactive governance, preventing statistical disclosure before deployment. This implementation demonstrates strong potential for cross-departmental metric sharing in healthcare while maintaining compliance and auditability. The system also promotes role-based access control (RBAC), supports zero-trust data architectures, and aligns with national data modernization goals by ensuring that metric pipelines are explainable, privacy-preserving, and AI-auditable by design. Unlike prior works that rely on runtime data access to flag privacy violations, the proposed framework performs static, explainable detection at the query-level, enabling pre-execution protection and audit readiness

