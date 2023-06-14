st.write('Exploratory Data Analysis (EDA) and Logistic Regression Model')


st.subheader('Sample Data')
st.write(df.head())


st.subheader('Data Shape')
st.write("Number of rows:", df.shape[0])
st.write("Number of columns:", df.shape[1])

st.subheader('Target Class Distribution')
st.write(df['target'].value_counts())


X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

st.subheader('Model Accuracy')
st.write("Accuracy:", accuracy)

confusion_mat = confusion_matrix(y_test, y_pred)
st.subheader('Confusion Matrix')
st.write(confusion_mat)
