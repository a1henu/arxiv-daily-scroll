---
layout: default
title: PrivPRISM: Automatically Detecting Discrepancies Between Google Play Data Safety Declarations and Developer Privacy Policies
---

# PrivPRISM: Automatically Detecting Discrepancies Between Google Play Data Safety Declarations and Developer Privacy Policies
**arXiv**：[2603.09214v1](https://arxiv.org/abs/2603.09214) · [PDF](https://arxiv.org/pdf/2603.09214.pdf)  
**作者**：Bhanuka Silva, Dishanika Denipitiyage, Anirban Mahanti, Aruna Seneviratne, Suranga Seneviratne  

**一句话要点**：提出PrivPRISM框架以自动检测Google Play数据安全声明与隐私政策间的不一致

**关键词**：隐私政策分析, 数据安全声明, 自动检测框架, 语言模型应用, 移动应用合规

## 3 点简述
- 核心问题：Google Play应用的数据安全声明常与隐私政策矛盾，误导用户并违反法规一致性要求。
- 方法要点：结合编码器和解码器语言模型，系统提取并比较隐私政策与数据安全声明的细粒度数据实践。
- 实验或效果：评估7,770款热门移动游戏，发现近53%存在不一致，静态代码分析揭示隐私政策仅披露66.8%敏感数据访问。

## 摘要（原文）

> End-users seldom read verbose privacy policies, leading app stores like Google Play to mandate simplified data safety declarations as a user-friendly alternative. However, these self-declared disclosures often contradict the full privacy policies, deceiving users about actual data practices and violating regulatory requirements for consistency. To address this, we introduce PrivPRISM, a robust framework that combines encoder and decoder language models to systematically extract and compare fine-grained data practices from privacy policies and to compare against data safety declarations, enabling scalable detection of non-compliance. Evaluating 7,770 popular mobile games uncovers discrepancies in nearly 53% of cases, rising to 61% among 1,711 widely used generic apps. Additionally, static code analysis reveals possible under-disclosures, with privacy policies disclosing just 66.8% of potential accesses to sensitive data like location and financial information, versus only 36.4% in data safety declarations of mobile games. Our findings expose systemic issues, including widespread reuse of generic privacy policies, vague / contradictory statements, and hidden risks in high-profile apps with 100M+ downloads, underscoring the urgent need for automated enforcement to protect platform integrity and for end-users to be vigilant about sensitive data they disclose via popular apps.

