---
layout: default
title: Application of machine learning to predict food processing level using Open Food Facts
---

# Application of machine learning to predict food processing level using Open Food Facts
**arXiv**：[2512.17169v1](https://arxiv.org/abs/2512.17169) · [PDF](https://arxiv.org/pdf/2512.17169.pdf)  
**作者**：Nalin Arora, Aviral Chauhan, Siddhant Rana, Mahansh Aditya, Sumit Bhagat, Aditya Kumar, Akash Kumar, Akanksh Semar, Ayush Vikram Singh, Ganesh Bagler  

**一句话要点**：提出基于机器学习的食品加工等级预测方法，利用Open Food Facts数据集实现大规模分类。

**关键词**：食品加工等级分类, 机器学习预测, Open Food Facts数据集, 营养成分分析, NOVA分类系统, 健康与环境影响

## 3 点简述
- 核心问题：超加工食品与健康和环境问题相关，需高效分类食品加工等级。
- 方法要点：使用LightGBM等模型，基于营养成分数据训练，实现NOVA分类。
- 实验或效果：LightGBM准确率达80-85%，有效区分加工等级，并揭示营养与环境关联。

## 摘要（原文）

> Ultra-processed foods are increasingly linked to health issues like obesity, cardiovascular disease, type 2 diabetes, and mental health disorders due to poor nutritional quality. This first-of-its-kind study at such a scale uses machine learning to classify food processing levels (NOVA) based on the Open Food Facts dataset of over 900,000 products. Models including LightGBM, Random Forest, and CatBoost were trained on nutrient concentration data. LightGBM performed best, achieving 80-85% accuracy across different nutrient panels and effectively distinguishing minimally from ultra-processed foods. Exploratory analysis revealed strong associations between higher NOVA classes and lower Nutri-Scores, indicating poorer nutritional quality. Products in NOVA 3 and 4 also had higher carbon footprints and lower Eco-Scores, suggesting greater environmental impact. Allergen analysis identified gluten and milk as common in ultra-processed items, posing risks to sensitive individuals. Categories like Cakes and Snacks were dominant in higher NOVA classes, which also had more additives, highlighting the role of ingredient modification. This study, leveraging the largest dataset of NOVA-labeled products, emphasizes the health, environmental, and allergenic implications of food processing and showcases machine learning's value in scalable classification. A user-friendly web tool is available for NOVA prediction using nutrient data: https://cosylab.iiitd.edu.in/foodlabel/.

