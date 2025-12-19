---
layout: default
title: Machine Learning Algorithms: Detection Official Hajj and Umrah Travel Agency Based on Text and Metadata Analysis
---

# Machine Learning Algorithms: Detection Official Hajj and Umrah Travel Agency Based on Text and Metadata Analysis
**arXiv**：[2512.16742v1](https://arxiv.org/abs/2512.16742) · [PDF](https://arxiv.org/pdf/2512.16742.pdf)  
**作者**：Wisnu Uriawan, Muhamad Veva Ramadhan, Firman Adi Nugraha, Hasbi Nur Wahid, M Dantha Arianvasya, Muhammad Zaki Alghifari  

**一句话要点**：提出基于文本与元数据分析的机器学习算法，以检测印尼朝觐与副朝旅行机构的官方应用真实性。

**关键词**：文本分析, 元数据分析, 机器学习分类, 应用验证, 数字欺诈检测, 宗教旅游安全

## 3 点简述
- 核心问题：印尼朝觐与副朝服务数字化中，假冒移动应用导致财务损失和隐私风险。
- 方法要点：结合应用描述的TF-IDF文本分析和敏感权限元数据，使用SVM、随机森林和朴素贝叶斯分类器。
- 实验或效果：SVM算法表现最佳，准确率达92.3%，关键词和权限如READ PHONE STATE为关键特征。

## 摘要（原文）

> The rapid digitalization of Hajj and Umrah services in Indonesia has significantly facilitated pilgrims but has concurrently opened avenues for digital fraud through counterfeit mobile applications. These fraudulent applications not only inflict financial losses but also pose severe privacy risks by harvesting sensitive personal data. This research aims to address this critical issue by implementing and evaluating machine learning algorithms to verify application authenticity automatically. Using a comprehensive dataset comprising both official applications registered with the Ministry of Religious Affairs and unofficial applications circulating on app stores, we compare the performance of three robust classifiers: Support Vector Machine (SVM), Random Forest (RF), and Na"ive Bayes (NB). The study utilizes a hybrid feature extraction methodology that combines Textual Analysis (TF-IDF) of application descriptions with Metadata Analysis of sensitive access permissions. The experimental results indicate that the SVM algorithm achieves the highest performance with an accuracy of 92.3%, a precision of 91.5%, and an F1-score of 92.0%. Detailed feature analysis reveals that specific keywords related to legality and high-risk permissions (e.g., READ PHONE STATE) are the most significant discriminators. This system is proposed as a proactive, scalable solution to enhance digital trust in the religious tourism sector, potentially serving as a prototype for a national verification system.

